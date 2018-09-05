# Lunch Box creator


# -----------------------------------------> CLASS <--------------------------------------------------------------------


#Item class , items that can be added to the slots of a lunchbox
class LunchItem(object):
    """Creating items object to use by the lunchbox"""
    item = 0

# list of instance objects
    itemlist = []

# list by type

    meallist = []
    vegylist = []
    fruitlist = []
    dairylist =[]
    dessertlist = []

# Create an instance user input
    @staticmethod
    def userinstance():
        print("Creating Lunch Item  instance")
        lunchitem_instance = input("What is the Lunch Item title?:\n")

        lunchitem_instance = LunchItem(lunchitem_instance, input("Enter your nutriment value: \n"),
                                 input("Enter your recipe instruction: \n"), input("Enter your lunch Item Type: \n"))
        print("--Lunch Item--")
        return lunchitem_instance

# Update how many there is
    @staticmethod
    def status():
        print("\nThe total number of Lunch item is ", LunchItem.item)

#Attribute of the class , Title, Nutitious value, type

    def __init__(self, title, nvalue, type):
        self.title = title
        self.nvalue = int(nvalue)
        self.type = type
        LunchItem.total +=1

    # Add to itemlist
        LunchItem.itemlist.append(self)

        if self.type == "meal" or self.type == "Meal":
            LunchItem.meallist.append(self)

        elif self.type == "vegy" or self.type == "Vegy":
                LunchItem.vegylist.append(self)

        elif self.type == "fruit" or self.type == "Fruit":
                LunchItem.fruitlist.append(self)

        elif self.type == "desert" or self.type == "Desert":
                LunchItem.dessertlist.append()

        else: self.type == "desert" or self.type == "Desert"
                LunchItem.dessertlist.append()

# Display the object when using print
    def __str__(self):
        rep = str.upper(self.title) + '\n\n'
        rep += str.rep += "Nutitious Value: \n" + self.nvalue + " \n\n"
        rep += "type: \n" + self.type + " \n\n"

#Display the object method
    def display(self):
        print("Title: \n\n" +self.title, "\n")
        print("value: \n\n" + self.nvalue + " \n")
        print("type: \n\n" + self.type + " \n")



# -----------------------------------------> functions <--------------------------------------------

# show what item there is
def itemlist():
    """Display all item """

    print("\t---Item Available---")
    for i, val in enumerate(LunchItem.itemlist):
        print("\t", i, val.title)

def vegylist():
    """Display all item """

    print("\t---Item Available---")
    for i, val in enumerate(LunchItem.vegylist):
        print("\t", i, val.title)

def fruitlist():
    """Display all item """

    print("\t---Item Available---")
    for i, val in enumerate(LunchItem.fruitlist):
        print("\t", i, val.title)

def dairylist():
    """Display all item """

    print("\t---Item Available---")
    for i, val in enumerate(LunchItem.dairylist):
        print("\t", i, val.title)

def desertlist():
    """Display all item """

    print("\t---Item Available---")
    for i, val in enumerate(LunchItem.desertlist):
        print("\t", i, val.title)


# -------------------------------------------> Helping Functions <----------------------------------------------------


# press enter to continue
def pressEnter():
    """Press enter to continue"""
    try:
        input("\nPress enter to continue")
        #   print("\n" * 15)
    except SyntaxError:
        pass

# clear IDLE
def clear():
    print("\n" * 15)
    print(
        "===========================================================================================================")


# -------------------------------------------------> MAIN MENU <--------------------------------------------------------

#main menu can i put that into its own class?
def menuPrincipal():
    """Main Menue"""
    selection = None

    while selection != "0":
        print("""
        Lunch BOX Creator 
        
        MAIN MENU
        
        LB
        1 - List All Available lunchbox
        2 - Create a Manual Lunchbox
        3 - Generate a Lunchbox
        
        4 - Go to Lunchbox Items Menue
        
        0 - EXIT
        
        """)

    selection = input("Selection: \n")

    if selection == "1":
        # TO DO : lunchbox object
        print("Lunch Box Available:")

        # TO DO : Lunch box object & generating auto lunchbox
    elif selection == "2":
        print ("Creating Manual Lunchbox")

        # TO DO : generating auto lunchbox
    elif selection == "3":
        print ("Generating Lunchbox")

        #TO DO : Lunch Item menu
    elif selection == "4":
        print ("Welcome to lunch item Menu")

    elif selection == "0":
        print("Quiting Recipe Main...")

    else:
        print("Input invalid choose 1-4 or 0")


