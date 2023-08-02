import random
import sys
import json
import requests

from loguru import logger
from web3 import Web3
from .account import Account
from config import BUNGEE_CONTRACTS, BUNGEE_ABI


class Bungee(Account):
    def __init__(self, private_key: str, chain: str, proxy: str) -> None:
        super().__init__(private_key, chain, proxy)

    def get_tx_data(self, value: float):

        tx = {
            "nonce": self.w3.eth.get_transaction_count(self.address),
            "value": 0,
            "gasPrice": self.w3.eth.gas_price,
            "gas": 0,
            "from": self.address,
            "to": self.address
        }

        tx["gas"] = self.w3.eth.estimate_gas(tx)
        tx["value"] = value
        del tx["to"]

        return tx

    def refuel(self, destination_chain: str, min_bridge: float, max_bridge: float):
        amount = int(random.uniform(min_bridge, max_bridge)*(10**18))
        min_amount, max_amount = self.get_bungee_limits(self.chain, destination_chain)
        print('min max', min_amount, max_amount, amount)

        if min_amount > amount > max_amount:
            logger.error(f"[{self.address}] Limit range amount for bridge {min_amount} – {max_amount} | {amount} ETH")
            sys.exit()

        logger.info(f"[{self.address}] Refuel {self.chain} –> {destination_chain} | {amount} ETH")

        tx_data = self.get_tx_data(amount)
        balance = self.w3.eth.get_balance(self.address)

        if amount >= balance:
            logger.error(f"[{self.address}] Insufficient funds!")
        else:
            with open('data/rpc.json') as file:
                RPC = json.load(file)

            contract = self.w3.eth.contract(address=Web3.to_checksum_address(BUNGEE_CONTRACTS[self.chain]),
                                         abi=BUNGEE_ABI)

            contract_txn = contract.functions.depositNativeToken(
                RPC[destination_chain]["chain_id"],  # destinationChainId
                self.address  # _to
            ).build_transaction(tx_data)

            signed_txn = self.sign(contract_txn)

            txn_hash = self.send_raw_transaction(signed_txn)

            self.wait_until_tx_finished(txn_hash.hex())

    @staticmethod
    def get_bungee_limits(from_chain, to_chain):
        with open('data/rpc.json') as file:
            RPC = json.load(file)

        from_chain_id = RPC[from_chain]['chain_id']
        to_chain_id = RPC[to_chain]['chain_id']

        response = requests.get("https://refuel.socket.tech/chains")
        data = json.loads(response.text)
        print(data)

        for i in range(len(data['result'])):
            if data['result'][i]['chainId'] == from_chain_id:
                infos = data['result'][i]['limits']

                try:

                    if [x for x in infos if x['chainId'] == to_chain_id][0] \
                            and [x for x in infos if x['chainId'] == to_chain_id][0]['isEnabled'] == True:

                        info = [x for x in infos if x['chainId'] == to_chain_id][0]
                        return int(info['minAmount']), int(info['maxAmount'])
                    else:
                        logger.error(f'рефуел из {from_chain} в {to_chain} невозможен')
                        return 0, 0

                except Exception as error:
                    logger.error(error)
