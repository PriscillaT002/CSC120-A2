'''
@File       : oo_resale_shop.py
@Time       : 2022/9/19 11:15 PM EST
@Author     : JCrouser edited by Priscilla Trejo
@Desc       : A python file that creates our resaleshop class for our inventory data. In this file I have included the oo sewuenced data for the resaleshop class, buy, sell, and print inventory methods.


'''

from computer import Computer
from typing import Dict, Union, Optional


  # This is the main Resaleshop class
class ResaleShop():

    ItemID = 0
    inventory = {}

    def __init__(self, ItemID: int, inventory):
        self.inventory: Dict[int, Computer] = inventory
        self.ItemID = ItemID


   # buy method 
    def buy(self, computer: Dict[str, Union[str,int,bool]]) -> list:
        global itemID
        # global inventory
        ItemID =+1
        self.inventory[ItemID] = computer
        return ItemID

       

    # sell method
    def sell(inventory, item_id: int ):
     if item_id in inventory:
        del inventory[item_id]
        print("Item", item_id, "sold!")
     else: 
        print("Item", item_id, "not")

   

    # inventory method
    def print_inventory(inventory):
    # If the inventory is not empty
     if inventory:
        # For each item
        for item_id in inventory:
            # Print its details
            print(f'Item ID: {item_id} : {inventory[item_id]}')
     else:
        print("No inventory to display.")





        







