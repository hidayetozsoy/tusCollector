from src.config import *
from src.funcs import *

def main():
    global account
    try:
        for address in PRIVATE_KEYS.keys():
            balance = checkBalance(address)
            if balance > FLOOR_LIMIT * pow(10,18):
                transferAmount = (balance - AMOUNT_LEFT) * pow(10,18) - TRANSFER_PRICE
                sendTx(address=address, dataInput="", value=int(transferAmount))

    except Exception as e:
        printn(e)
        
main()