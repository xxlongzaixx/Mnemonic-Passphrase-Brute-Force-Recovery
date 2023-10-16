from web3 import Web3
from eth_account import Account
import time

rpc = "https://rpc.ankr.com/eth"
filename = "phrase.txt"
timer = 0.3 # rest 0.3 seconds between rpc call

web3 = Web3(Web3.HTTPProvider(rpc))

Account.enable_unaudited_hdwallet_features()

def get_balance_from_mnemonic(mnemonic):
    try:
        acct = Account.from_mnemonic(mnemonic)
        address = acct.address

        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.from_wei(balance_wei, 'ether')

        return address, balance_eth
    except Exception as e:
        print(e)

with open(filename, 'r') as p_file:
    # Read each line and process it
    for line in p_file:
        words = line.strip().split()  # Split the line into words
        mnemonic = ' '.join(words)   # Join the words back into a string

        address, balance = get_balance_from_mnemonic(mnemonic)

        print(f"Mnemonic: {mnemonic}")
        print(f"Address: {address}")
        print(f"Balance: {balance} ETH")

        time.sleep(timer)
        if balance > 0:
            break
