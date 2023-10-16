from itertools import product
from eth_account import Account

"""
Generate all possible permutations of passphrases using the given words
and screen them to identify the valid ones
"""

filename = "phrase.txt"

# Define your mnemonic passphrases
word1 = ["person", "someone", "myself"]
word2 = ["fall", "drop"]
word3 = ["season", "quarter"]
word4 = ["enjoy", "excite", "love"]
word5 = ["tragic", "grief", "regret"]
word6 = ["crew", "team", "group"]
word7 = ["mind", "brain"]
word8 = ["dolphin", "squirrel"]
word9 = ["capable", "skill"]
word10 = ["arrange", "install"]
word11 = ["board", "slab", "panel"]
word12 = ["sound", "rhythm", "pitch"]

Account.enable_unaudited_hdwallet_features()

# Generate all combinations of the words
all_combinations = product(
    word1,
    word2,
    word3,
    word4,
    word5,
    word6,
    word7,
    word8,
    word9,
    word10,
    word11,
    word12,
)

with open(filename, "w") as p_file:
    for combination in all_combinations:
        new_mnemonic = " ".join(combination)

        try:
            print(new_mnemonic)

            acct = Account.from_mnemonic(new_mnemonic)
            private_key = acct._private_key.hex()

            # Get the Ethereum address
            address = acct.address

            p_file.write(f"{new_mnemonic}\n")
        except Exception as e:
            print(e)
