from modules import *

# RANDOM WALLETS MODE
RANDOM_WALLET = False  # True or False

# SLEEP MODE
IS_SLEEP = True  # True or False

SLEEP_FROM = 5  # Second
SLEEP_TO = 15  # Second

# PROXY MODE
USE_PROXY = False

# GWEI CONTROL MODE
CHECK_GWEI = False  # True or False
MAX_GWEI = 40


def generate_ERC20_wallets():
    """
    Generate ERC20 wallets
    """

    wait_from = 2       # пауза между генерацией кошелька в сек.
    wait_to = 5
    N = 100     # количество кошельков

    generate_ERC20(N, wait_from, wait_to)


def bridge_zksync(key, proxy):
    """
    Deposit from official bridge
    ______________________________________________________
    amount – Amount of bridge (2, 5), type in uniform(2, 5) | number after uniform() – decimal point
    """

    min_bridge = 0.001
    max_bridge = 0.002
    decimal = 4

    zksync = ZkSync(key, proxy)
    zksync.deposit(min_bridge, max_bridge, decimal)


def bridge_orbiter(key, proxy):
    """
    Bridge from orbiter
    ______________________________________________________
    from_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    to_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    ______________________________________________________
    amount – Amount of bridge (2, 5), type in uniform(2, 5) | number after uniform() – decimal point
    amount – Limit range amount for bridge – minimum 0.005, maximum 5
    """

    from_chain = "zksync"
    to_chain = "ethereum"

    min_bridge = 1
    max_bridge = 3
    decimal = 4

    orbiter = Orbiter(key, from_chain, proxy)
    orbiter.bridge(to_chain, min_bridge, max_bridge, decimal)


def swap_syncswap(key, proxy):
    """
    Make swap on syncswap

    from_token – Choose SOURCE token ETH/USDC | Select one
    to_token – Choose DESTINATION token ETH/USDC | Select one
    ______________________________________________________
    amount – Amount of swap (2, 5), type in uniform(2, 5) | number after uniform() – decimal point
    """

    from_token = "ETH"
    to_token = "USDC"

    min_swap = 0.001
    max_swap = 0.002
    decimal = 4

    syncswap = SyncSwap(key, proxy)
    syncswap.swap(from_token, to_token, min_swap, max_swap, decimal)


def swap_mute(key, proxy):
    """
    Make swap on mute
    ______________________________________________________
    from_token – Choose SOURCE token ETH/USDC | Select one
    to_token – Choose DESTINATION token ETH/USDC | Select one
    ______________________________________________________
    amount – Amount of swap (2, 5), type in uniform(2, 5) | number after uniform() – decimal point
    """

    from_token = "USDC"
    to_token = "ETH"

    min_swap = 1
    max_swap = 2
    decimal = 4

    mute = Mute(key, proxy)
    mute.swap(from_token, to_token, min_swap, max_swap, decimal)


def swap_spacefi(key, proxy):
    """
    Make swap on space.fi
    ______________________________________________________
    from_token – Choose SOURCE token ETH/USDC | Select one
    to_token – Choose DESTINATION token ETH/USDC | Select one
    ______________________________________________________
    amount – Amount of swap (2, 5), type in uniform(2, 5) | number after uniform() – decimal point
    """

    from_token = "ETH"
    to_token = "USDC"

    min_swap = 0.001
    max_swap = 0.002
    decimal = 4

    spacefi = SpaceFi(key, proxy)
    spacefi.swap(from_token, to_token, min_swap, max_swap, decimal)


def bungee(key, proxy):
    """
    Bungee refuel
    ______________________________________________________
    from_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    to_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    ______________________________________________________
    """

    from_chain = "zksync"
    to_chain = "gnosis"

    min_bridge = 0.000003
    max_bridge = 0.000005

    bungee = Bungee(key, from_chain, proxy)
    bungee.refuel(to_chain, min_bridge, max_bridge)

def okx_withdraws(address, proxy):
    """
    OKX withdraw
    ______________________________________________________
    from_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    to_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    ______________________________________________________
    """

    symbolWithdraw = "ETH"  # символ токена BNB, ETH, MATIC
    network = "zkSync Era"

    amount_from = 0.004
    amount_to = 0.004
    FEE = 0.0003  # комса на вывод
    SUB_ACC = False
    account = 'main'

    okx_withdraw(address, symbolWithdraw, network, amount_from, amount_to, account, FEE, SUB_ACC)
