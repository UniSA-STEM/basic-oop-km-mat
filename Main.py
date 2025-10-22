"""
File: main.py
Description: <A brief description of this Python module.>
Author: Karl Matillano
ID: 110336447
Username: matky024
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
from Rig import Rig

def main():

#    ct = Asset("CryptoToken")
    ds = Asset("Data Spike")
#    rd = Asset("Removable Drive")
    sc = Asset("Security Chip")
    hp = Asset("Hardware Patch")

    print("START")

    #create players
    player = Hacker("Player")
    npc1 = Hacker("NPC")

    #generate rig
    player.rig = Rig("Player_Rig")
    npc1.rig = Rig("NPC_Rig")

    #test
    print(player)
    print(player.rig)
    print(npc1)
    print(npc1.rig)

    print("\nattack 1")
    player.launch_data_spike(npc1)
    npc1.launch_data_spike(player)

    print(player)
    print(player.rig)
    print(npc1)
    print(npc1.rig)

    print("\nattack 2")

    player.launch_data_spike(npc1)
    npc1.launch_data_spike(player)

    print(player)
    print(player.rig)
    print(npc1)
    print(npc1.rig)

    print("\nextraction")
    player.extract_asset(npc1)

    player.show_inventory()
    player.rig.show_storage()

    #generate asset
    print("\nGenerate Asset")
    player.rig.generate_asset()
    player.rig.generate_asset()

    #show inventory after generate asset
    player.show_inventory()
    player.rig.show_storage()

    #upgrade rig
    print("\nUpgrade Rig")
    player.inventory.append(hp)
    player.show_inventory()
    player.upgrade_rig()
    player.show_inventory()
    print(player.rig)

    #test encryption. give player data spikes
    print("\nEncryption")
    player.inventory.append(sc)
    player.inventory.append(ds)
    player.show_inventory()

    print(player.rig)
    player.encrypt_asset(ds)
    player.decrypt_asset(ds)

    player.show_inventory()
if __name__ == "__main__":
    main()