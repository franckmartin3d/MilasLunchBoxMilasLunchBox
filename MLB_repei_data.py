# Mila's lunchbox recipe feature


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
        Recipe.rlist.append(self)

        #Add to breakfast list:
        if self.type == "breakfast" or self.type == "Breakfast":
            Recipe.breakfastList.append(self)

        # Add to Lunch list :
        elif self.type == "lunch" or self.type == "Lunch":
            Recipe.lunchList.append(self)

        #Add to dinner list
        else:
            Recipe.dinnerList.append(self)


    def __str__(self):
        #rep = Recipes
        rep =  str.upper(self.title) + " \n\n"
        rep += "ingredient: \n" + self.ingredient + " \n\n"
        rep += "instruction: \n" + self.instruction + " \n\n"
        rep += "Type: \n" + self.type + " \n\n"
        return rep

    def display(self):
        print("Title: \n\n", self.title, "\n")
        print("Ingredient: \n\n" + self.ingredient + " \n")
        print("Instruction: \n\n" + self.instruction + " \n")


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
     #   print("\n" * 15)
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
    for i, val in enumerate(Recipe.rlist):
        print("\t", i, val.title)



def breakfastList():
    """Display breakfast recepi"""

    print("\t---Breakfast RECEPI---")
    for i, val in enumerate(Recipe.breakfastList):
        print("\t", i, val.title)



def lunchList():
    """Display lunch recepi"""

    print("\t---LUNCH RECEPI---")
    for i, val in enumerate(Recipe.lunchList):
        print("\t", i, val.title)



def dinnerList():
    """Display Dinner recepi"""
    print("\t---Dinner RECEPI---")
    for i, val in enumerate(Recipe.dinnerList):
        print("\t", i, val.title)

#####################################################        DATA        ################
from csv import reader
from csv import writer


def data_rlist():
    with open("recepi.csv", "w") as file:
        csv_writer = writer(file)
        csv_writer.writerow(Recipe.rlist)


########################################################     Sub-menu ##################################################

# Type submenu
def typeSubmenu():
    """Submenu to select the type of recepi"""


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
            displaymenu('b',"typeSubmenu")

        elif typeChoice == "2":
            print("All AVAILABLE LUNCH RECEPI\n")
            listID = "l"
            lunchList()
            displaymenu('l',"typeSubmenu")


        elif typeChoice == "3":
            print("All AVAILABLE DINNER RECEPI\n")
            listID = "d"
            dinnerList()
            displaymenu('d',"typeSubmenu")


        elif typeChoice == "0":
            print("Loading Main Menu\n")
            clear()
            menuPrincipal()

        else:
            print("Input invalide choose 1-4 or 0")

    position = "typeSubmenu"
    return position

# display menu
def displaymenu(listID, position):
    """Selection Main Menu"""

    choice = None

    while choice != "0":
        print ("""
        
        
        ############################
        # 1 - Select a Recipe      #
        # 0 - Back to Last Menu    #
        ############################

        """)
        choice = input("Choice:\n ")
        if choice == "1":
            recepiIndex = int(input("Display the following recipe: (#)\n "))

            #Breakfast list menu
            if listID == "b":
                if recepiIndex in range(len(Recipe.breakfastList)):
                    recepi_instance = Recipe.breakfastList[recepiIndex]
                    recepi_instance.display()
                else:
                    print("\nINVALID SELECTION\nLOADING MAIN MENU!")
                    clear()
                    menuPrincipal()


            #All list menu
            elif listID == "a":
                if recepiIndex in range(len(Recipe.rlist)):
                    recepi_instance = Recipe.rlist[recepiIndex]
                    recepi_instance.display()
                else:
                    print("\nINVALID SELECTION\nLOADING MAIN MENU!")
                    clear()
                    menuPrincipal()

            #Lunch list menu
            elif listID == "l":
                if recepiIndex in range(len(Recipe.lunchList)):
                    recepi_instance = Recipe.lunchList[recepiIndex]
                    recepi_instance.display()
                else:
                    print("\nINVALID SELECTION\nLOADING MAIN MENU!")
                    clear()
                    menuPrincipal()

            # Lunch list menu
            elif listID == "d":
                if recepiIndex in range(len(Recipe.dinnerList)):
                    recepi_instance = Recipe.dinnerList[recepiIndex]
                    recepi_instance.display()
                else:
                    print("\nINVALID SELECTION\nLOADING MAIN MENU!")
                    clear()
                    menuPrincipal()


        elif choice == "0":

            #return to type submenu
            if position == "typeSubmenu":
                typeSubmenu()

            #return to main menu
            elif position == "mainmenu":
                menuPrincipal()

        else:
            print("Input invalide choose 1 or 0")

    position = "displaymenu"
    return position



def editmenu():
    """ Edit Menu"""

    selection = None

    while selection != "0":
        print("""

            EDIT MAIN MENU

            1 - Display All Recipe to edit
            0 - Exit
            """)

        selection = input("Select: \n")

        if selection == "1":
            print("Here Are all the Recipe Available to Edit!\n")
            recepilist()
            recepiIndex = int(input("What recipe do you want to Edit: # "))

            if recepiIndex in range(len(Recipe.rlist)):
                    recepi_instance = Recipe.rlist[recepiIndex]
                    recepi_instance.display()

                    print("debug here")

                    editRecepi(recepi_instance)
                    return recepi_instance
            else:
                print("\nINVALID SELECTION\nLOADING MAIN MENU!")

    position = "editmenu"
    return

def editRecepi(recepi_instance):
    """Edit a recepie"""
    selection = None

    while selection != "0":
        print("""

        EDIT SECTION

        1 - Title
        2 - Ingredient
        3 - Instruction
        4 - Type
        0 - Back to mainmenu
                """)

        selection = input("Select: \n")

        #replce title
        if selection == "1":
            recepi_instance.title = input("Changing title from " + recepi_instance.title + " to :\n")

            print("Title is now:", recepi_instance.title)

        #replace Ingredient
        elif selection == "2":
            recepi_instance.ingredient = input("Changing ingredient from " + recepi_instance.ingredient + " to :\n")

            print("Ingedient is now:", recepi_instance.ingredient)

        #replace Instruction
        elif selection == "3":
            recepi_instance.instruction = input("Changing Instruction from " + recepi_instance.instruction + " to :\n")

            print("instruction is now:", recepi_instance.instruction)

        # replace type
        elif selection == "4":
            recepi_instance.type = input("Changing type from " + recepi_instance.type + " to :\n")

            print("type is now:", recepi_instance.type)

        else:
            menuPrincipal()


#MainMenue

def menuPrincipal():
    """Main menu"""
    selection = None

    while selection != "0":
        print("""
        
        RECEPI MAIN MENU
        
        1 - List all Recipe
        2 - List by Type
        3 - Add new Recipe
        4 - Edit a Recipe
        5 - debug display saved data
        0 - Exit
        """)

        selection = input("Select: \n")

        if selection == "1":
            print("Here Are all the Recipe Available!\n")
            #print(Recipe.rlist)
            clear()
            recepilist()
            displaymenu("a","mainmenu")

        elif selection == "2":
            #print("Display Recepi Sub-Menu\n")
            clear()
            typeSubmenu()

        elif selection =="3":
            print("Add a new recipe!")
            clear()
            Recipe.userinstance()

        elif selection == "4":
            print("Edit recipe")
            editmenu()

        elif selection == "5":
            print("Saved data")
            data_rlist()

        elif selection == "0":
            print("Quiting Recipe Main...")

        else:
            print("Input invalid choose 1-4 or 0")

    position = "mainmenu"
    return position

###############################################main################################################################3####

# Test Recipe
testDinner1 = Recipe("test Spaghetti", "Pasta, Tomato, Sauce, mince", "1:boil pasta 2:do the sauce","dinner" )
testDinner1 = Recipe("test Penne romanov", "Pasta, Tomato, Sauce, mince", "1:boil pasta 2:do the sauce","dinner" )

testBreakfast1 = Recipe("test Oat_Bowl", "Oat , Milk", "1: Put oat on stove\n2: pour milk in it \n3:wait until bubles", "Breakfast")
testBreakfast2 = Recipe("test toast", "bread, peanut butter", "1: toat the bread 2: spread the pb","breakfast")

testLunch2 = Recipe("test sandwich", "bread ham salami mayo", "Do the sanwich", "lunch")
testLunch1 = Recipe("KD", "milk & KD", "do the kd", "lunch")
#recipe3 = Recipe.userinstance()
#recepi2.display()
#Recepi.breakfastList[0]
#Recipe.display(Recipe.breakfastList[0])
menuPrincipal()














