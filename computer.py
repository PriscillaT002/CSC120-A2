'''
@File       : computer.py
@Time       : 2022/9/19 11:15 PM EST
@Author     : JCrouser edited by Priscilla Trejo
@Desc       : A python file that creates our computer class for our resale shop inventory data. In this file I have included the oo sequenced data for the computer class, refurbish, update price, and create computer methods.

'''

from typing import Dict, Union, Optional

# Computer class
class Computer:
    

    def __init__(self, description : str ,processor_type: int, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: float) -> None:
    

    # attributes
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    # refurbish method
    def refurbish(inventory, item_id: int, new_os: Optional[str] = None):
     if item_id in inventory:
        computer = inventory[item_id] # locate the computer
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff

        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS
     else:
        print("Item", item_id, "not found. Please select another item to refurbish.")


    # update price method
    def update_price(inventory, item_id: int, new_price: int):
     if item_id in inventory:
        inventory[item_id]["price"] = new_price
     else:
        print("Item", item_id, "not found. Cannot update price.")


    # new computer method 
    def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
     return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }



      

   