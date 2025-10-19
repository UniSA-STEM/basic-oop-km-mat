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
        self.Trace_Level = 0 #Hackers have a trace level, which starts at 0 and increases when they perform risky actions
        self.Exposed = False #If the trace level exceeds a threshold(e.g., 5), the hacker becomes exposed,

    def acquire_rig:
        if self.cryptotoken < 1:  #check CryptoToken Count
            print("You need to acquire a rig.") #if not enough token, display fail message and end method
            return
        self.cryptotoken -= 1 #remove one token counter prior to activation
        self.rig = Rig(rig_name) #calls Rig class
        print("{self.name} Rig Acquired and now ACTIVE") #. print a message announcing the acquisition
