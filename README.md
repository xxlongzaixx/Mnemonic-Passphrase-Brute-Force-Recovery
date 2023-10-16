# Mnemonic-Passphrase-Brute-Force-Recovery
A Python script designed to brute force all specified permutations in order to check the balance or attempt to recover an address.


Requirement
-----------------
* python

Dependencies 
-----------------

```
pip install -r requirements.txt
```

Usage
-----------------
Step 1 : Run the following command will output all possible permutations of the passphrase to phrase.txt, it will screen through and removed the invalid ones.
```
py src/screen.py
```
Step 2: Run the following command to check the balance of each mnemonic passphrase account and stop when it finds a balance greater than 0.
```
py src/balance.py
```
