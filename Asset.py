"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Karl Matillano
ID: 110336447
Username: matky024
This is my own work as defined by the University's Academic Misconduct Policy.
"""
ASSET_LIBRARY = [ #define library in a list
    ("CryptoToken", "Used to acquire or repair rigs"),
    ("Data Spike", "Used in battles"),
    ("Removable Drive", "Used for extraction"),
    ("Security Chip", "Used to encrypt/decrypt assets"),
    ("Hardware Patch", "Used to upgrade rigs")
]

class Asset:

    def __init__(self, name, description, encrypted = False): #By default, assets are not encrypted.
        self.name = name
        self.encrypted = encrypted #
        self.description = ("Unknown") #initiate description as unknown then
        for n, desc in ASSET_LIBRARY:  #loop through asset list to fetch description from tuple  
            if n == name:
                self.description = desc
                break

    def encrypt(self):  #switch encrypted status to True
        self.encrypted = True

    def decrypt(self):  #switch encrypted status to False
        self.encrypted = False