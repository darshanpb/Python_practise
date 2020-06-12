# -*- coding: utf-8 -*-
''' 
List to Dictionary Function for Fantasy Game Inventory Imagine that a vanquished dragon’s loot is represented as a list of strings
like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:
def addToInventory(inventory, addedItems):
# your code goes here
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
The previous program (with your displayInventory() function from the previous project) would output the following:
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48 '''
from ex4 import getItems #using function from previous work
def addToInventory(inv,dragonLoot):
    for item in dragonLoot:
        if item not in inv.keys():
            inv.setdefault(item,1)
        else:
            inv[item]+=1
    return inv

''' 
def getItems(item):
    Total_items = 0
    for key, val in item.items():
        print(str(val)+":"+key)
        Total_items += val
    print("Total number of Items in Inventory:"+str(Total_items)) '''

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
getItems(inv)
