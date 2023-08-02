import requests
import json
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

print(wallet, web3.eth.account.from_key(key).address)