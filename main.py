'''
@File       : main.py
@Time       : 2022/9/19 11:15 PM EST
@Author     : JCrouser edited by Priscilla Trejo
@Desc       : A python file that intakes the data from the computer.py and oo_resale_shop.py files and outputs inventory data.

'''

# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union
from computer import Computer
from oo_resale_shop import ResaleShop

# Import the functions we wrote in procedural_resale_shop.py
# from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""

def main():
    
    # First, let's make a computer
    OO_computer = Computer.create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )



    # Add it to the resale store's inventory
    print("Buying", OO_computer["description"])
    print("Adding to inventory...")
    # theShop = ResaleShop()
    computer_id = ResaleShop.buy(OO_computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    #inventory = ResaleShop.print_inventory(ResaleShop)
    ResaleShop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    Computer.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    ResaleShop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()
