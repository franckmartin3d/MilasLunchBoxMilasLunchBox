# Mila's lunchbox recepi feature


#Class

#recepi object
class Recipe(object):
    """Creating recipes object"""
    total = 0
    rlist = []

    # Create an instance user input
    @staticmethod
    def userinstance():
        print("Creating a recipe instance")
        recepi_instance = input("What recepi name?")

        recepi_instance = Recipe(input("Enter your recipe Title: \n"), input("Enter your recipe ingredient: \n"), input("Enter your recipe instruction: \n"),input("Enter your recipe Type: \n") )

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
        Recipe.rlist.append(self.title)


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
        print("instruction: " + self.ingredient + " \n")

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

# List of all recepi

# class Rlist(object):
# """Creat a list of all recepi"""
#     def __ini__(self, name):
#         self.name = name
#         self.list = []
#         for i in titles:

def recepilist():
    for i in Recipe.rlist:
        print("Title:", Recipe.rlist)



#function
# Main Menu

def menuPrincipal() :
    """Main menu"""
    selection = None

    while selection != "0":
        print("""
        
        RECEPI MAIN Menue
        
        1 - List all Recepi
        2 - List by Type
        3 - Add new Recepi
        4 - Edit a recepi
        0 - Exit
        """)

        selection = input("Select: ")

        if selection == "1":
            print("Here Are all the Recepi Available!\n")
            #print(Recipe.rlist)
            recepilist()

        elif selection == "2":
            print("Recepi by type:")

        elif selection =="3":
            print("Add a new recepi!")

        elif selection == "4":
            print("Edit recepi")

        elif selection == "0":
            print("Quiting Recepi Main...")

###############################################main##################

# Default recepi
recepi1 = Recipe("Spagati", "Pasta, Tomato, Sauce, mince", "1:boil pasta\n2:do the sauce","dinner" )
recepi2 = Recipe("Oat Bowl", "Oat , Milk", "1: Put oat on stove\n2: pour milk in it \n3:wait until bubles", "Breakfast")
#recipe3 = Recipe.userinstance()

menuPrincipal()













