"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Karl Matillano
ID: 110336447
Username: matky024
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Hacker:
    def __init__(self, name):
        self.name = name #something cryptic and stylish
        self.inventory = [] #hacker inventory
        self.cryptotoken = 1 #always start with one
        self.rig = None #no rig to start with
        self.trace_level = 0 #Hackers have a trace level, which starts at 0 and increases when they perform risky actions
        self.exposed = False #If the trace level exceeds a threshold(e.g., 5), the hacker becomes exposed,

    def acquire_rig(self, rig_name):
        if self.cryptotoken < 1:  #check CryptoToken Count
            print("You need to acquire a rig.") #if not enough token, display fail message and end method
            return
        self.cryptotoken -= 1 #remove one token counter prior to activation
        self.rig = Rig(rig_name) #calls Rig class
        print("{self.name} Rig Acquired and now ACTIVE") #. print a message announcing the acquisition

    def launch_data_spike(self, target_name):
        #check if hacker does not have a rig and show message if so
        if not self.rig: print("You need to acquire a rig.")
            return

        #call release_asset on rig for a "Data Spike"
        launch_spike = self.rig.release_asset("Data Spike")
        #check if spike returns true, else no data spike message
        if not launch_spike:
            print("You have no Data Spikes left!")
            return
        self.trace_level += 1
        target_name.rig.take_damage()
        print(f"{self.name} has attacked {target name}!"
              f"Trace level is at {self.trace_Level})

    def extract_assets(self, target_name):
        #check if other rig is broken
        if not target_name.rig.broken:
            print("{target_name} is not broken... extraction unsuccessful}")
            return

        #check for removable drive in broken rig, if not, show no removable drive message
        removable_drive = self.rig.release_asset("Removable Drive")
        if not removable_drive:
            print("{target_name} has no Removable Drive")
            return

        #make a list of things in rig that are not enccrypted
        loot = [stuff for stuff in target_name.rig.storage if not stuff.encrypted]
        #if there is, add to own inventory
        for item in loot:
            self.inventory.append(item)
        #create a list of only encrypted items in the target storage
        #replace target rig storage with encrypted only items list
        target_name.rig.storage [stuff for stuff in target.rig.storage if stuff.encrypted]
        print(f"{self.name} has extracted {len(loot)} items from {target_name}")

    def encrypt_asset(self, asset_name):
        #look for security chip
        chip = None
        for stuff in self.inventory:
            if stuff.name == "Security Chip":
                chip = stuff
                break
        #if no chip is found, show message
        if not chip:
            print(f"{self_name} lacks Security Chip")
            return False
        #remove chip from inventory
        self.inventory.remove(chip)
        #encrypt selected item
        for stuff in self.inventory:
            if stuff.name == asset_name:
                stuff.encrypt()
                print(f"{stuff.asset_name} encrypted.")
                return True
        #if for whatever reason the target asset is not found, add chip back in
        if chip is not None:
            self.inventory.append(chip)
        print("Asset not found, chip returned.")
        return False

    def decrypt_asset(self, asset_name):
        # look for security chip
        chip = None
        for stuff in self.inventory:
            if stuff.name == "Security Chip":
                chip = stuff
                break
        # if no chip is found, show message
        if not chip:
            print(f"{self_name} lacks Security Chip")
            return False
        # remove chip from inventory
        self.inventory.remove(chip)
        # encrypt selected item
        for stuff in self.inventory:
            if stuff.name == asset_name:
                stuff.decrypt()
                print(f"{stuff.asset_name} decrypted.")
                return True
        # if for whatever reason the target asset is not found, add chip back in
        if chip is not None:
            self.inventory.append(chip)
        print("Asset not found, chip returned.")
        return False

    def upgrade_rig(self):
        #if hacker has no rig, show error message
        if not self.rig:
            print("You need to acquire a rig.")
            return False
        #call rig upgrade method
        return self.rig.upgrade(self)

    def repair_rig(self):
        # if hacker has no rig, show error message
        if not self.rig:
            print("You need to acquire a rig.")
        #call rig repair method
        return self.rig.repair(self)

    def store_to_rig(self, asset_name):
        #if hacker has no rig, show error message
        if not self.rig:
            print("You have no rig t store assets in.")
            return False
        #check capacity of rig, if full return error message
        if self.rig.storage >= self.rig.max_storage_size():
            print(f"{self.rig.rig_name}'s storage is full and cannot store {asset_name}"
            return False
        #find item in inventory
        check_asset = None
        for stuff in self.inventory:
            if stuff.name == asset_name:
                check_asset = stuff
                break
        #if item is not found, show error message
        if not check_asset:
            print(f"{self.name} does not have {asset_name} in inventory.")
            return False
        #check if asset is encrypted, and if so display error message
        if check_asset.encrypted:
            print(f"{asset_name} is encrypted and cannot be stored unless decrypted.")
            return False
        #remove from inventory to store into rig
        self.inventory.remove(check_asset)
        #call store_asset from rig method
        verify = self.rig.store_asset(check_asset)
        #if verification fail, put back item into hacker inventory
        if not verify:
            self.inventory.append(check_asset)
            return False

        return True

    def retrieve_asset(self, asset_name):
        #call release_asset method from rig
        stuff = rig.release_asset(asset_name)
        #if it fails, show error message
        if not stuff:
            print(f"{rig.rig_name} does not have {asset_name} in storage.")
        #upon success, add to inventory and show success message
        self.inventory.append(stuff)
        print(f"{self.name} has retrieved {stuff.name}.")
        return True

    def __str__(self):
        rig_name = self.rig_name if self.rig else "None"
        return (f"Hacker {self.rig_name} | Rig:{rig_name} | Trace {self.trace_level} Tokens: {self.cryptotoken} }

