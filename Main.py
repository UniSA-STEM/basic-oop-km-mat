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

if __name__ == "__main__":
    main()