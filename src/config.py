MAIN_ADDRESS = "0xf6463F3C5E2DCe879eE61E005A0Ad15601838A84" #address of the account that coins will be sent to

PRIVATE_KEYS = { #private keys of the addresses that TUS will be sent from. Main address shouldn't be involved
    "0x82A323000D50CABaEd045A71FDE88e01a8b082d8":"58995c0f29e038d54d94868b8592edc1cbe88f076e24aa91b1a54b5d463317df",
    "0x4043D2508C591f57C1C0d36CF227be5a3ace83d4":"686e075ee398432d1ea14f9acabd93e695f77404bc51d800dab3c0c1aa02fe14",
}

AMOUNT_LEFT = 150 * pow(10,18) #amount of TUS that will be left at the address to maintain the game.
FLOOR_LIMIT = 300 * pow(10,18) #floor limit for transfer. if the amount is less than floor limit, transfer will not be executed.

GAS_PRICE_LIMIT = 20000 * pow(10,9)
GAS_LIMIT = 300000
MAX_PRIORITY_FEE_PER_GAS = 0

TRANSFER_PRICE = 0.21 * pow(10,18)

RPC_URL = "https://subnets.avax.network/swimmer/mainnet/rpc" #swimmer network
CHAIN_ID = 73772 #swimmer network