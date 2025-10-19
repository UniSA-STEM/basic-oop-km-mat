"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Karl Matillano
ID: 110336447
Username: matky024
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Rig:
    def __init__(self, rig_name):
        self.rig_name = rig_name
        self.damage_counter = 0 #start at zero damage counter
        self.broken = False #start not broken
        self.storage = [ #starting asset of a rig
            Asset("Data Spike"),
            Asset("Data Spike"),
            Asset("Removable Drive")]
        self.upgrade_level = 0  #start at 0 upgrade level
        self.max_storage_size = 3 #base capacity at level 0

    def max_storage_size(self):     #increase max capacity along with upgrade level
        return self.max_storage_size + self.upgrade_level

    def upgrade(self):  #upgrade the rig
        self.upgrade_level += 1 #by one
        print(f"{self.rig_name} upgraded to {self.upgrade_level} level! Capacity upgraded to {self.max_storage_size}!")


    def take_damage(self):
        self.damage_counter += 1

    def condition(self):
        condi = "Broken" if self.broken else "Pristine"
        return f"{condi} {self.damage_counter} damage (Level {self.upgrade_level})"