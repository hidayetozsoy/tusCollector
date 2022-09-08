from src.config import *
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import ContractLogicError
from time import sleep

def printn(*text):
    print()
    print(*text)

#sleeps for x seconds and prints it
def sleepy(secs):
    printn(f"Sleeping {secs} secs...")
    sleep(secs)

#return the given address's balance
def checkBalance(address):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    balance = w3.eth.getBalance(address)
    return balance

#sends transaction from given address with given dataInput and value, sends type2 EIP-1559 transaction.
def sendTx(address, dataInput="", value=0):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    account = w3.eth.account.from_key(PRIVATE_KEYS[address])
    nonce = w3.eth.getTransactionCount(account.address)
    rawTransaction = {
            "chainId" : hex(CHAIN_ID),
            "from": address,
            "maxFeePerGas": GAS_PRICE_LIMIT,
            "maxPriorityFeePerGas":MAX_PRIORITY_FEE_PER_GAS,
            "gas": GAS_LIMIT, 
            "to": MAIN_ADDRESS,
            "value": value,
            "data" : dataInput,
            "nonce" : nonce,
            "type":2,
        } 
    printn("Sending EIP-1559 tx...")
    try:
        gas_estimate = w3.eth.estimate_gas(rawTransaction) #checks if the contract will throw error.
    except ContractLogicError as e:
        printn(f"Tx is expected to be fail. Not sending...\n{e}")
        return
    signedTxn = account.sign_transaction(rawTransaction) 
    w3.eth.send_raw_transaction(signedTxn.rawTransaction) 
    printn("EIP-1559 tx sent...")