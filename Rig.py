"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Karl Matillano
ID: 110336447
Username: matky024
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random

from Asset import ASSET_LIBRARY, Asset


class Rig:
    def __init__(self, rig_name):
        self.rig_name = rig_name
        self.damage_counter = 0 #start at zero damage counter
        self.durability = 2 #start at 2 for level 0 rig
        self.broken = False #start not broken
        self.storage = [ #starting asset of a rig
            Asset("Data Spike"),
            Asset("Data Spike"),
            Asset("Removable Drive")]
        self.upgrade_level = 0  #start at 0 upgrade level
        self.max_storage_size = 3 #base capacity at level 0

    def rig_repair(self, Hacker):
        if self.damage_counter == 0: #check if there is damage to begin with.
            print("No damage detected") #does not proceed with repair if rig has no damage
            return
        if Hacker.cryptotoken < 1: #check if hacker has cryptotoken to use as currency for repair
            print(f"{Hacker.name} Not Enough Cryptotoken to repair {self.rig_name}. Repair is Aborted.")
            return
        Hacker.cryptotoken -= 1 #removes one cryptotoken for repair
        self.damage_counter = 0 #resets damage counter to 0 upon repair
        self.broken = False     #remove broken status
        print(f"Cryptotoken consumed for repair..."
              f"{self.rig_name} is now fully repaired!")
        return True

    def storage_size(self):   #returns storage size
        return len(self.storage)

    def max_capacity(self):     #increase max capacity along with upgrade level
        return self.max_storage_size + self.upgrade_level * 2

    def max_durability(self):       #increase max durability along with upgrade level
        return self.durability + self.upgrade_level

    def upgrade(self):  #upgrade the rig
        hardwarepatch = None
        # check storage if it has a hardware patch
        for stuff in self.storage:
            if stuff.name == "Hardware Patch":
                hardwarepatch = stuff
                break
        # if no hardware patch found, send no patch detected message
        if not hardwarepatch:
            print("No hardware patch detected")
            return False
        # if patch found, remove one hardwarepatch
        self.storage.remove(hardwarepatch)
        self.upgrade_level += 1 #by one
        #show updated new stats upon upgrade
        print(f"{self.rig_name} upgraded to Level {self.upgrade_level}!")
        print(f"→ Max Storage increased to {self.max_storage_size} items.")
        print(f"→ Max Durability increased to {self.durability} damage points.")
        return True

    def take_damage(self):
        self.damage_counter += 1    #each hit increases damage by 1 w

        # assess broken status
        if self.damage_counter >= self.durability:  #broken if damage counter exceeds durability
            self.broken = True
            print(f"{self.rig_name} is now broken!")
        else:
            print(f"{self.rig_name} has taken 1 damage."
                  f"(HP left: {self.durability} durability left!")

    def condition(self):
        condi = "Broken" if self.broken else "Pristine" #
        return f"{condi} {self.damage_counter} damage (Level {self.upgrade_level})"

    def generate_asset(self):
        if self.storage_size >= self.max_capacity:
            print(f"{self.rig_name}'s storage capacity is full")
            return
        # fetch a random tuple in library as generated asset
        name, description = random.choice(ASSET_LIBRARY)
        newasset = Asset(name)
        # show name and description of generated asset
        print(f"{self.rig_name} generated {newasset.name} ({newasset.description})!")
        return True

    def store_asset(self, h_asset):
        #check if storage size is full
        if self.storage_size() >= self.max_capacity():
            print(f"{self.rig_name}'s storage capacity is full")
            return
        #add new asset to storage
        self.storage.append(h_asset)
        print(f"{self.rig_name} stored {h_asset.name}")
        return True

    def release_asset(self, h_asset):
        #return asset back to hacker's inventory
        for stuff in self.storage:
            if stuff.name == h_asset.name:
                self.storage.remove(stuff)
                return stuff
        print(f"{self.rig_name} has released {h_asset.name}")
        return True

    def __str__(self):
        return(f"Rig: {self.rig_name} | {self.condition()} (Level {self.upgrade_level})"
               f"Storage: {self.durability}/{self.max_durability()}"
               f"Durability: {self.damage_counter}/{self.max_durability})")
