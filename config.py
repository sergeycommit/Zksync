import json

with open('data/rpc.json') as file:
    RPC = json.load(file)

with open('data/abi/zksync_bridge.json') as file:
    ZKSYNC_BRIDGE_ABI = json.load(file)

with open('data/abi/erc20_abi.json') as file:
    ERC20_ABI = json.load(file)

with open("private_keys.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]

with open("withdraw_addresses.txt", "r") as file:
    WITHDRAW_ADDRESSES = [row.strip() for row in file]

with open("proxy.txt", "r") as file:
    PROXIES = [row.strip() for row in file]

with open("data/abi/syncswap/router.json", "r") as file:
    SYNCSWAP_ROUTER_ABI = json.load(file)

with open("data/abi/spacefi/router.json", "r") as file:
    SPACEFI_ROUTER_ABI = json.load(file)

with open("data/abi/mute/router.json", "r") as file:
    MUTE_ROUTER_ABI = json.load(file)

with open("data/abi/bungee_abi.json", "r") as file:
    BUNGEE_ABI = json.load(file)

ZKSYNC_BRIDGE = "0x32400084c286cf3e17e7b677ea9583e60a000324"

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

ZKSYNC_TOKENS = {
    "ETH": "0x5aea5775959fbc2557cc8789bc1bf90a239d9a91",
    "USDC": "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4"
}

SYNCSWAP_CONTRACTS = {
    "router": "0x2da10A1e27bF85cEdD8FFb1AbBe97e53391C0295",
    "WETH": "0x5aea5775959fbc2557cc8789bc1bf90a239d9a91",
}

SPACEFI_CONTRACTS = {
    "router": "0xbE7D1FD1f6748bbDefC4fbaCafBb11C6Fc506d1d"
}

MUTE_CONTRACTS = {
    "router": "0x8B791913eB07C32779a16750e3868aA8495F5964"
}

SYNCSWAP_POOL = "0x80115c708E12eDd42E504c1cD52Aea96C547c05c"

ORBITER_CONTRACT = "0x80C67432656d59144cEFf962E8fAF8926599bCF8"

BUNGEE_CONTRACTS = {
    'ethereum'      : '0xb584D4bE1A5470CA1a8778E9B86c81e165204599',
    'optimism'      : '0x5800249621da520adfdca16da20d8a5fc0f814d8',
    'bsc'           : '0xbe51d38547992293c89cc589105784ab60b004a9',
    'arbitrum'      : '0xc0e02aa55d10e38855e13b64a8e1387a04681a00',
    'polygon'       : '0xAC313d7491910516E06FBfC2A0b5BB49bb072D91',
    'polygon_zkevm' : '0x555a64968e4803e27669d64e349ef3d18fca0895',
    'zksync'        : '0x7Ee459D7fDe8b4a3C22b9c8C7aa52AbadDd9fFD5',
    'avalanche'     : '0x040993fbf458b95871cd2d73ee2e09f4af6d56bb',
    'gnosis'        : '0xBE51D38547992293c89CC589105784ab60b004A9',
    'fantom'        : '0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB',
}
