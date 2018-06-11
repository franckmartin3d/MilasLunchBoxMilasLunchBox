# Mila's lunchbox recepi feature


#Class

#recepi object
class Recipe(object):
    """Creating recipes object"""
    total = 0

    #list of instance
    rlist = []
    breakfastList = []
    lunchList = []
    dinnerList = []


    # Create an instance user input
    @staticmethod
    def userinstance():
        print("Creating a recipe instance")
        recepi_instance = input("What is the recepi title?:\n")

        recepi_instance = Recipe(recepi_instance, input("Enter your recipe ingredient: \n"), input("Enter your recipe instruction: \n"),input("Enter your recipe Type: \n") )
        print("--RECEPI CREATED--")
        pressEnter()
        return recepi_instance


    @staticmethod
    def status():
        print("\nThe total number of recepi is ", Recipe.total)

    def __init__(self, title, ingredient, instruction, type ):
        self.title = title
        self.ingredient = ingredient
        self.instruction = instruction
        self.type = type
        Recipe.total +=1

        # Add to All List
        Recipe.rlist.append(self.title)

        #Add to breakfast list:
        if self.type == "breakfast" or self.type == "Breakfast":
            Recipe.breakfastList.append(self.title)

        # Add to Lunch list :
        elif self.type == "Lunch" or self.type == "Lunch":
            Recipe.lunchList.append(self.title)

        #Add to dinner list
        else:
            Recipe.dinnerList.append(self.title)


    def __str__(self):
        #rep = Recipes
        rep =  str.upper(self.title) + " \n\n"
        rep += "ingredient: \n" + self.ingredient + " \n\n"
        rep += "instruction: \n" + self.instruction + " \n\n"
        rep += "Type: \n" + self.type + " \n\n"
        return rep

    def display(self):
        print("Title: \n" ,self.title, "\n")
        print("ingredient: " + self.ingredient + " \n")
        print("instruction: " + self.instruction + " \n")

    #edit
    def changeTitle(self):
        newtitle = input("Change title from", self.title, "to: \n")

        if newtitle == "":
            print("Recepie needs a title")
        else:
            self.title = newtitle

    def changeIngredient(self):
        newtitle = input("Change ingredient from", self.ingredient, "to: \n")

        if newtitle == "":
            print("Recepie needs ingredient")
        else:
            self.ingredient = newtitle


##############################FUNCTION##################################################################################
# Utilities
# press enter to continue
def pressEnter():
    """Press enter to continue"""
    try:
        input("\nPress enter to continue")
        print("\n" * 15)
    except SyntaxError:
        pass
#clear IDLE
def clear():
    print("\n" * 15)
    print("===========================================================================================================")


# List of all recepi
def recepilist():
    """Display all recepi"""

    print("\t---RECEPI---")
    for i in Recipe.rlist:
        print("\t", i)

    pressEnter()

def breakfastList():
    """Display breakfast recepi"""

    print("\t---Breakfast RECEPI---")
    for i, val in enumerate(Recipe.breakfastList):
        print("\t", i, val)

    pressEnter()

def lunchList():
    """Display lunch recepi"""

    print("\t---LUNCH RECEPI---")
    for i, val in enumerate(Recipe.lunchList):
        print("\t", i, val)

    pressEnter()

def dinnerList():
    """Display Dinner recepi"""
    print("\t---Dinner RECEPI---")
    for i, val in enumerate(Recipe.dinnerList):
        print("\t", i, val)

    pressEnter()

# Sub-menu

# Type submenu
def typeSubmenu():

    typeChoice = None

    while typeChoice != "0":
        print("""

               RECEPI TYPE TO DISPLAY

                1 - Breakfast.
                2 - Lunch.
                3 - Dinner.
                0 - Back to main menu


                    """)

        typeChoice = input("Select: \n")

        if typeChoice == "1":
            print("All AVAILABLE BREAKFAST RECEPI\n")
            listID = "b"
            breakfastList()
            displaymenu('b')

        elif typeChoice == "2":
            print("All AVAILABLE LUNCH RECEPI\n")
            clear()
            lunchList()

        elif typeChoice == "3":
            print("All AVAILABLE DINNER RECEPI\n")
            clear()
            dinnerList()

        elif typeChoice == "0":
            print("Loading Main Menu\n")
            clear()
            menuPrincipal()

        else:
            print("Input invalide choose 1-4 or 0")


# display menue
def displaymenu(listID):
    """Selection Main Menu"""
    choice = None

    while choice != "0":
        print ("""
        1 - Select a recepi
        0 - Back to last menu

        """)
        choice = input("Choice: ")
        if choice == "1":
            recepiIndex = int(input("What recepi do you want to display: "))
            if listID == "b":
                print(listID)
                print(Recipe.breakfastList[recepiIndex])
                # recepi_instance = str((Recipe.breakfastList[recepiIndex]))





        elif choice == "0":
            typeSubmenu()

# def selectobject():
#     """Select object in list and display it"""
#
#
#     print(r)
#     selectedItem = None
#
#     for object in Recipe.rlist:
#
#
#     while selectedItem != "0"

# Main Menu

def menuPrincipal() :
    """Main menu"""
    selection = None

    while selection != "0":
        print("""
        
        RECEPI MAIN MENU
        
        1 - List all Recepi
        2 - List by Type
        3 - Add new Recepi
        4 - Edit a recepi
        0 - Exit
        """)

        selection = input("Select: \n")

        if selection == "1":
            print("Here Are all the Recepi Available!\n")
            #print(Recipe.rlist)
            clear()
            recepilist()

        elif selection == "2":
            #print("Display Recepi Sub-Menu\n")
            clear()
            typeSubmenu()

        elif selection =="3":
            print("Add a new recepi!")
            clear()
            Recipe.userinstance()

        elif selection == "4":
            print("Edit recepi")

        elif selection == "0":
            print("Quiting Recepi Main...")

        else:
            print("Input invalide choose 1-4 or 0")

###############################################main##################

# Default recepi
recepi1 = Recipe("Spagati", "Pasta, Tomato, Sauce, mince", "1:boil pasta\n2:do the sauce","dinner" )
Oat_bowl = Recipe("Oat_Bowl", "Oat , Milk", "1: Put oat on stove\n2: pour milk in it \n3:wait until bubles", "Breakfast")
#recipe3 = Recipe.userinstance()
#recepi2.display()
#Recepi.breakfastList[0]
#Recipe.display(Recipe.breakfastList[0])
menuPrincipal()














