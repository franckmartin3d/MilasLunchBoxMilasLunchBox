# Franck 8/02/2019


import os
import subprocess


# -----------------------------------------> CLASS <--------------------------------------------------------------------
# Item class , items that can be added to the slots of a lunchbox
class Store(object):
    # Storing items
    itemsCount = 0

    listItem = []

    # type list
    listDairy = []
    listFruit = []
    listVeg = []
    listMain = []
    listDesert = []

    def __init__(self, title):
        self.title = title

    # display the Store
    def display(self):
        print("You have one Storage Named: \n" + self.title + "\n")
        print("You have this many items in Storage: \n", Store.itemsCount)
        print("\n")

    def displayAll(self):
        print("this is the list of all items")
        for x in Store.listItem:
            print(x)


class FoodItem(object):

    # properties

    def __init__(self, title, type, calories):
        self.title = title
        self.type = type
        self.calories = calories

        # file the global info
        # add count
        Store.itemsCount += 1

        # Add to list
        Store.listItem.append(self)

        # Appen type list Dairy, fruit , veg , main desert
        if self.type == "dairy" or self.type == "Dairy":
            Store.listDairy.append(self)

        elif self.type == "veg" or self.type == "Veg":
            Store.listVeg.append(self)

        elif self.type == "fruit" or self.type == "Fruit":
            Store.listFruit.append(self)

        elif self.type == "main" or self.type == "Main":
            Store.listMain.append(self)

        else:
            Store.listDesert.append(self)

    def display(self):
        print("Item: " + self.title)
        print("Type: " + self.type)
        print("Caloriess:", self.calories)
        print("\n")


# -----------------------------------------> Functions <--------------------------------------------------------------------

def displayItem(listSelection):
    """Display all recepi"""

    if listSelection == 1:
        choice = Store.listItem

    elif listSelection == 2:
        choice = Store.listDairy

    elif listSelection == 3:
        choice = Store.listVeg

    elif listSelection == 4:
        choice = Store.listFruit

    elif listSelection == 5:
        choice = Store.listMain

    else:
        choice = Store.listDesert

    print("\t")
    for i, val in enumerate(choice):
        print("\t", i, val.title)


# # -----------------------------------------> Run test<--------------------------------------------------------------------
# # testing Store class
# fridge = Store("Fridge")
#
# #testing food items
#
#
# Apple = FoodItem("Apple", "Fruit", 50)
# Banana = FoodItem("Banana", "Fruit", 44)
# IceCream = FoodItem("IceCream", "desert", 600)
# Brocoli = FoodItem("Brocoli", "veg", 44)
# Sandwich = FoodItem("Sandwich", "main", 66)
# yogurt = FoodItem("yogurt", "dairy", 88)
#
# Apple.display()
#
# #use the store display
# fridge.display()
#
# #display all list
# print("List of all item in storage")
# displayItem(1)
#
#
# print("List of all item in dairy")
# displayItem(2)
#
# print("List of all item in veg")
# displayItem(3)
#
# print("List of all item in fruit")
# displayItem(4)
#
# print("List of all item in main")
# displayItem(5)
#
# print("List of all item in desert")
# displayItem(7)

# -----------------------------------------> Main menu <--------------------------------------------------------------------

header = "\
.____     ____ __________  _________   ___ ___   __________ ________  ____  ___ \n\
|    |   |    |   \      \ \_   ___ \ /   |   \  \______   \\_____  \ \   \/  / \n\
|    |   |    |   /   |   \/    \  \//    ~    \  |    |  _/ /   |   \ \     / \n\
|    |___|    |  /    |    \     \___\    Y    /  |    |   \/    |    \/     \ \n\
|_______ \______/\____|__  /\______  /\___|_  /   |______  /\_______  /___/\  \ \n\
        \/               \/        \/       \/           \/         \/      \_/   \n"

colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
}


def colorize(string, color):
    if not color in colors: return string
    return colors[color] + string + '\033[0m'


def storage():
    print("You Selected Storage()")
    input("Press [Enter] to continue...")
    storageMenue()


def lunchbox():
    print("You select lunchbox")
    input("Press [Enter] to continue...")


menuItems = [
    {"Storage(items)": storage},
    {"Lunchbox": lunchbox},
    {"Exit": exit},
]


def main():
    while True:
        subprocess.call("cls", shell=True)  # windows
        print(colorize(header, 'pink'))
        print(colorize('version 0.1\n', 'green'))
        for item in menuItems:
            print(colorize("[" + str(menuItems.index(item)) + "] ", 'blue') + list(item.keys())[0])
        choice = input(">> ")
        try:
            if int(choice) < 0: raise ValueError
            # Call the matching function
            list(menuItems[int(choice)].values())[0]()
        except (ValueError, IndexError):
            pass


# -------------------------------------Storage Menu----------------------------------------------------------------------
substorage = """
  ___  _
 / __|| |_  ___  _ _  __ _  __ _  ___ 
 \__ \|  _|/ _ \| '_|/ _` |/ _` |/ -_ 
 |___/ \__|\___/|_|  \__,_|\__, |\___|
                           |___/    
   \n """

colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
}


def createStorage():
    print("You select Create a storage")
    input("Press [Enter] to continue...")

    storageName = input("whats the name of your storage?\n")
    storage = Store(storageName)
    storage.display()
    input("Press [Enter] to continue...")


def foodItemMenu():
    print("You select Items menu")
    input("Press [Enter] to continue...")




menuItemsB = [
    {"Create Storage": createStorage},
    {"Create food items": foodItemMenu},
    {"Exit": exit},
]


def storageMenue():
    while True:
        subprocess.call("cls", shell=True)  # windows
        print(colorize(substorage, 'pink'))
        print(colorize('version 0.1\n', 'green'))
        for item in menuItemsB:
            print(colorize("[" + str(menuItemsB.index(item)) + "] ", 'blue') + list(item.keys())[0])
        choice = input(">> ")
        try:
            if int(choice) < 0: raise ValueError
            # Call the matching function
            list(menuItemsB[int(choice)].values())[0]()
        except (ValueError, IndexError):
            pass


# #-------------------------------------Items Menu----------------------------------------------------------------------
# subheader = """
#
# .___   __
# |   |_/  |_   ____    _____    ______
# |   |\   __\_/ __ \  /     \  /  ___/
# |   | |  |  \  ___/ |  Y Y  \ \___ \
# |___| |__|   \___  >|__|_|  //____  >
#                  \/       \/      \/
#
#    \n """
#
# colors = {
#         'blue': '\033[94m',
#         'pink': '\033[95m',
#         'green': '\033[92m',
#         }
#
#
#
# def createFoodItem():
#     print("You select Create a food Item")
#     input("Press [Enter] to continue...")
#
# def displayAll():
#     print("You select Items menu")
#     input("Press [Enter] to continue...")
#
# def displayCategories():
#     print("You select Items menu")
#     input("Press [Enter] to continue...")
#
#
# def backSub():
#
#     storageMenu()
#
# itemsSelection = [
#     { "Create a storage space": createFoodItem},
#     { "Food Items menu": displayAll},
#     { "Display selected list": displayCategories},
#     { "Back": backSub},
#     { "Exit": exit },0
# ]
# def itemsMenue():
#     while True:
#         subprocess.call("cls", shell=True)  # windows
#         print(colorize(subheader, 'pink'))
#         print(colorize('version 0.1\n', 'green'))
#         for item in itemsSelection:
#             print(colorize("[" + str(itemsSelection.index(item)) + "] ", 'blue') + list(item.keys())[0])
#         choice = input(">> ")
#         try:
#             if int(choice) < 0 : raise ValueError
#             # Call the matching function
#             list(itemsSelection[int(choice)].values())[0]()
#         except (ValueError, IndexError):
#             pass
#


if __name__ == "__main__":
    main()
