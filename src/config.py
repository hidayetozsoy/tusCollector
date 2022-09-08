MAIN_ADDRESS = "0xf6463F3C5E2DCe879eE61E005A0Ad15601838A84" #address of the account that coins will be sent to

PRIVATE_KEYS = { #private keys of the addresses that TUS will be sent from. Main address shouldn't be involved
    "0xcf80bc3d82513035b4a3f3fa7322d91e643c5e13":"",
    "0x2b2aafa7c46d4854540fe6d955a5c9a5ccc1fcd6":"",
    "0xca25ed5b1de6db099ca55087a2727a803620f5b7":"",
    "0xe9eaf20cfec1ce6c9b73c7fed4514218dd441124":""
}

AMOUNT_LEFT = 150 #amount of TUS that will be left at the address to maintain the game.
FLOOR_LIMIT = 300 #floor limit for transfer. if the amount is less than floor limit, transfer will not be executed.

GAS_PRICE_LIMIT = 20000 * pow(10,9)
GAS_LIMIT = 300000
MAX_PRIORITY_FEE_PER_GAS = 0

TRANSFER_PRICE = 0.21 * pow(10,18)

RPC_URL = "https://subnets.avax.network/swimmer/mainnet/rpc" #swimmer network
CHAIN_ID = 73772 #swimmer network