import random
import sys
import time

from config import *

from settings import *
from utils.gas_cheker import wait_gas
from utils.get_proxy import get_proxy


def get_module():
    result = input(
        "Select a number of method to get started: \r\n "
        "   0. Generate ERC20 wallets\r\n "
        "   1. Make bridge ZkSync\r\n "
        "   2. Make bridge on Orbiter\r\n "
        "   3. Make swap on SyncSwap\r\n "
        "   4. Make swap on Mute\r\n "
        "   5. Make swap on Space.fi\r\n"
        "   6. Make refuel on Bungee\r\n"
        "   7. OKX withdraw\r\n "
        "   your num choose: ")

    return int(result)


def main(module, key, proxy):
    if module == 0:
        generate_ERC20_wallets()
    if module == 1:
        bridge_zksync(key, proxy)
    elif module == 2:
        bridge_orbiter(key, proxy)
    elif module == 3:
        swap_syncswap(key, proxy)
    elif module == 4:
        swap_mute(key, proxy)
    elif module == 5:
        swap_spacefi(key, proxy)
    elif module == 6:
        bungee(key, proxy)
    elif module == 7:
        okx_withdraws(key, proxy)


if __name__ == '__main__':
    print("\nSubscribe to me –– https://t.me/my_utils\n")

    module = get_module()

    if RANDOM_WALLET:
        random.shuffle(ACCOUNTS)

    if module == 7:
        ACCOUNTS = WITHDRAW_ADDRESSES

    for j, key in enumerate(ACCOUNTS):
        proxy = None
        if USE_PROXY:
            proxy = get_proxy()
        if CHECK_GWEI:
            wait_gas()
        main(module, key, proxy)

        if j + 1 < len(ACCOUNTS) and IS_SLEEP:
            time.sleep(random.randint(SLEEP_FROM, SLEEP_TO))

    print("\nSubscribe to me –– https://t.me/my_utils\n")
