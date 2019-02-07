
#Lunchbocx for dice









# -----------------------------------------> Store Items <-------------------------------------------------------------
# to store an item and put these item in a list
# list should be accesible and can be sorted by properties


# -----------------------------------------> Global <-------------------------------------------------------------





# -----------------------------------------> Classs <-------------------------------------------------------------

class Fridge(object):
    """Creating a item object"""
 # list of instance object

    itemCount = 0
    # Type of item
    listItem = []

    # type list
    listDairy = []
    listFruit = []
    listVeg = []
    listMain = []
    listDesert = []


    #properties
    def __init__(self, title, type, calories):
        self.title = title
        self.type = type
        self.calories = calories

        # file the global info
        #add count
        Items.itemCount += 1

        # Add to list
        Items.listItem.append(self)

        #Appen type list Dairy, fruit , veg , main desert
        if self.type == "dairy" or "Dairy":
            Items.listDairy.append(self)

        elif self.type == "veg" or "Veg":
            Items.listVeg.append(self)

        elif self.type == "fruit" or "Fruit":
            Items.listFruit.append(self)

        elif self.type == "main" or "Main":
            Items.listMain.append(self)

        else:
            Items.listDesert.append(self)


    # Display the object when using print
    def __str__(self):
        #item
        item = str.upper(self.title) + "\n"
        item += "type: \n" + self.type + "\n"
        item += "calories: \n" + self.calories + "\n"
        return item

    def display(self):
        print("Title: " + self.title + "\n")
        print("Type: " + self.type + "\n")
        print("Calories: " + self.calories + "\n")

 #Create an instance user input
    @staticmethod
    def userinstance():
        print("Creating an item...")
        item_instance = input("")
        Item_instance = Items(item_instance, input("Enter your Item Title: \n"), input("Enter your Item Type: \n"),input("Enter Item's Calories: \n") )
        print("--Item CREATED--")
        pressEnter()
        return item_instance

    @staticmethod
    def status(self):
        print("The number of items is :", Items.itemCount + '\n')

# -----------------------------------------> functions <-------------------------------------------------------------

# List of all
def displayItem(listSelection):
    """Display all recepi"""

    if listSelection == 1:
        choice = Items.listItem

    elif listSelection == 2:
        choice = Items.listDairy

    elif listSelection == 3:
        choice = Items.listVeg

    elif listSelection == 4:
        choice = Items.listFruit

    elif listSelection == 5:
        choice = Items.listMain

    else:
        choice = Items.listDesert

    print("\t")
    for i, val in enumerate(choice):
        print("\t", i, val.title)


# -----------------------------------------> Menu (To do) <-------------------------------------------------------------

def testItemMenue():
    # debug
    print("\t all of the item")
    for i, val in enumerate(Items.listItem):
        print("\t", i, val.title)

    print("\t all of the item veg")
    for i, val in enumerate(Items.listVeg):
        print("\t", i, val.title)

    print("\t all of the item fruit")
    for i, val in enumerate(Items.listFruit):
        print("\t", i, val.title)

    print("\t all of the item dairy")
    for i, val in enumerate(Items.listDairy):
        print("\t", i, val.title)

    "main menue for testing"
    Choice = None
    print("""
    
    Test item menue
    
    1 - display number of items
    2 - list all items
    3 - list all veg 
    4 - list all fruit 

    
    
    """)

    choice = input("Selection: \n")
    if choice == "1":
        print("the number of item is: ", Items.itemCount)
        testItemMenue()

    if choice == '2':
        print(" Here is all the items")
        displayItem(1)

    if choice == '3':
        print(" Here is the item in veg")
        displayItem(3)

    if choice == '4':
        print(" Here is the item in fruit")
        displayItem(4)






# -----------------------------------------> Maint (test) <-------------------------------------------------------------




#Test items

testItem1 = Items("Carrots", "Veg", 55)
testItem2 = Items("Strawberry", "Fruit", 55)
testItem3 = Items("potato", "Veg", 55)

testItemMenue()