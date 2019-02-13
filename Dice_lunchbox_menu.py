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

# -----------------------------------------> Header<--------------------------------------------------------------------
header_main = "\
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
header_storage = """
  ___  _
 / __|| |_  ___  _ _  __ _  __ _  ___ 
 \__ \|  _|/ _ \| '_|/ _` |/ _` |/ -_ 
 |___/ \__|\___/|_|  \__,_|\__, |\___|
                           |___/    
   \n """

header_lunch = """
  _                      _       _                 
 | |                    | |     | |                
 | | _   _  _ __    ___ | |__   | |__    ___ __  __
 | || | | || '_ \  / __|| '_ \  | '_ \  / _ \\ \/ /
 | || |_| || | | || (__ | | | | | |_) || (_) |>  < 
 |_| \__,_||_| |_| \___||_| |_| |_.__/  \___//_/\_\
                                                   
                                                
 \n"""
header_items = """

.___   __
|   |_/  |_   ____    _____    ______
|   |\   __\_/ __ \  /     \  /  ___/
|   | |  |  \  ___/ |  Y Y  \ \___ 
|___| |__|   \___  >|__|_|  //____  >
                 \/       \/      \/

   \n """

header_stats = """
       _          _        
      | |        | |       
  ___ | |_  __ _ | |_  ___ 
 / __|| __|/ _` || __|/ __|
 \__ \| |_| (_| || |_ \__ |
 |___/ \__|\__,_| \__||___/
                                                     
\n"""

header_list = """                
 _  _       _   
| ||_| ___ | |_ 
| || ||_ -||  _|
|_||_||___||_|  
                \n"""

header_creation = """


                      _    _            
  __  _ _  ___  __ _ | |_ (_) ___  _ _  
 / _|| '_|/ -_)/ _` ||  _|| |/ _ \| ' \ 
 \__||_|  \___|\__,_| \__||_|\___/|_||_|
                                        
\n"""



def colorize(string, color):
    if not color in colors: return string
    return colors[color] + string + '\033[0m'

menuState = "main"
# -----------------------------------------> Menue <--------------------------------------------------------------------
# -----------------------------------------> Main <--------------------------------------------------------------------
#storage menu
def main_storage():
    print("You Selected Storage Menu")
    input("Press [Enter] to continue...")
    main("storage")

#  lunchbox menu
def main_lunchbox():
    print("You select lunchbox Menu")
    input("Press [Enter] to continue...")
    main("lunch")


# item menu
def main_item():
    print("You select Item Menue")
    input("Press [Enter] to continue...")
    main("item")


menuItems_main = [
    {"Storage Menu": main_storage},
    {"Lunchbox Menu": main_lunchbox},
    {"Item Menu": main_item},
    {"Exit": exit}, ]

# -------------------------------------Storage Menu----------------------------------------------------------------------

def storage_create():
    print("You select Create a storage")
    input("Press [Enter] to continue...")
    subprocess.call("cls", shell=True)  # windows
    storageName = input("whats the name of your storage?\n")
    storage = Store(storageName)
    storage.display()

    input("Press [Enter] to continue...")
    return storage


def storage_stats():
    print("You select Items menu")
    input("Press [Enter] to continue...")
    main("stats")


def storage_main():
    print("You select main menu")
    input("Press [Enter] to continue...")
    main("main")


menuItems_storage = [
    {"Create Storage": storage_create},
    {"Stats Menu": storage_stats},
    {"Back to main Menu":storage_main},
    {"Exit": exit},]

#-------------------------------------Lunch Menu----------------------------------------------------------------------

def lunch_create():
    print("You select Create lunch box ")
    input("Press [Enter] to continue...")
    main("creation")

def lunch_list():
    print("You select list menu")
    input("Press [Enter] to continue...")
    main("list")

def lunch_main():
    print("You select main menu")
    input("Press [Enter] to continue...")
    main("main")

menuItems_lunch = [
    { "Lunch Creation Menu": lunch_create},
    { "List Menu": lunch_list},
    { "Back": lunch_main},]

#-------------------------------------Items Menu----------------------------------------------------------------------

def items_createFoodItem():
    print("You select Create a food Item")
    input("Press [Enter] to continue...")

def items_list():
    print("You select Create a food Item")
    input("Press [Enter] to continue...")
    main("list")

def item_back():
    print("You select Create a food Item")
    input("Press [Enter] to continue...")
    main("main")

menuItems_Items = [
    { "Create an item": items_createFoodItem},
    { "List menu": items_list},
    { "Back": item_back},]

#-------------------------------------stats Menu----------------------------------------------------------------------
def stats_items():
    print ("Selected 'How many item is in storage'")
    input("Press [Enter] to continue...")

def stats_list():
    print ("List Menu'")
    input("Press [Enter] to continue...")
    main("list")

def stats_main():
    print("Back to main Menu")
    input("Press [Enter] to continue...")
    main("main")


menuItems_stats = [
    { "Storage Stats": stats_items},
    { "List menu": stats_list},
    { "Back": stats_main},]


# -------------------------------------list Menu----------------------------------------------------------------------
def list_Allitems():
    print("Selected 'How many item is in storage'")
    input("Press [Enter] to continue...")


def list_veg():
    print("List all Vegetable items'")
    input("Press [Enter] to continue...")

def list_fruit():
    print("List all fruit items'")
    input("Press [Enter] to continue...")

def list_dairy():
    print("List all dairy items'")
    input("Press [Enter] to continue...")

def list_main():
    print("List all Main corse items'")
    input("Press [Enter] to continue...")

def list_desert():
    print("List all desert items'")
    input("Press [Enter] to continue...")


def list_back():
    print("Back to main Menu")
    input("Press [Enter] to continue...")
    main("main")


menuItems_list = [
    {"List All Items": list_Allitems},
    {"Vegetable": list_veg},
    {"Fruit": list_fruit},
    {"Main": list_main},
    {"Desert": list_desert},
    {"Dairy": list_dairy},
    {"Back": stats_main}, ]
# -------------------------------------Creation Menu----------------------------------------------------------------------
def creation_custom():
    print("Creating a custom lunchbox'")
    input("Press [Enter] to continue...")

def creation_random():
    print("Creating a custom lunchbox'")
    input("Press [Enter] to continue...")


def creation_main():
    print("back to main menu")
    input("Press [Enter] to continue...")
    main("main")

menuItems_creation = [
    {"Create a custom lunchbox": creation_custom},
    {"Create a Random lunchbox": creation_random},
    {"Back tro main menue": creation_main},]

# -----------------------------------------> Variable <--------------------------------------------------------------------
# a variable to show what menu u are in


#main menu
\\to do
def main(menuState):
    if menuState == "main":
        # set the  header
        header = header_main
        menuItems = menuItems_main

    # Storage menu
    elif menuState == "storage":
        # set the  header
        header = header_storage
        menuItems = menuItems_storage

    # Lunch Menu
    elif menuState == "lunch":
        # set the header
        header = header_lunch
        menuItems = menuItems_lunch

    #items Menu
    elif menuState == "items":
        # set the header
        header = header_items
        menuItems = menuItems_Items

    # Stats
    elif menuState == "stats":
        # set the header
        header = header_stats
        menuItems = menuItems_stats

    elif menuState == "list":
        # set the header
        header = header_list
        menuItems = menuItems_list

    elif menuState == "creation":
        header = header_creation
        menuItems = menuItems_creation

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



if __name__ == "__main__":
    main("main")
