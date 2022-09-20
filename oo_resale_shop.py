from computer import Computer
from typing import Dict, Union, Optional



class ResaleShop():

    ItemID = 0
    inventory = {}

    def __init__(self, ItemID: int, inventory):
        self.inventory: Dict[int, Computer] = inventory
        self.ItemID = ItemID

        

    def buy(self, computer) -> int:
        # global itemID
        # global inventory
        self.ItemID =+1
        self.inventory[self.ItemID] = computer
        return self.ItemID

       

    #method sell

    def sell(inventory, item_id: int ):
     if item_id in inventory:
        del inventory[item_id]
        print("Item", item_id, "sold!")
     else: 
        print("Item", item_id, "not")

   

    #method inventory

    def print_inventory(inventory):
    # If the inventory is not empty
     if inventory:
        # For each item
        for item_id in inventory:
            # Print its details
            print(f'Item ID: {item_id} : {inventory[item_id]}')
     else:
        print("No inventory to display.")





        







