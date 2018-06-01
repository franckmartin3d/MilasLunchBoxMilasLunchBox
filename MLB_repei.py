# Mila's lunchbox recepi feature


class Recepi_list(object):
    """Creating recepi dictionary"""
    #Create a empty dictionary
    def create_empty(self):
        """input:Nothing
        Output: 3 empty list"""

        self.list = {}

    #add new recepi to list
    def add_recepi(self):
        """input: nothing
        output: add a recepi"""
        # get the title of the recepei
        print("ADD A RECEPI")
        title = input("Recepi Title:")
        if title not in self.list:
            description = input("\n What is the descrition of the recepi:")
            self.list[title] = description
            print("\n", title, "Has been added.")
        else:
            print("the", title ," recepi is already in the list, try to edit it")
        return title, description

    def show_recepi(self):
        """show all recepi in global recepi"""
        print("Here are all your recepi")
        for key in self.list:
            print(key)


class Recipe(object):
    """Creating recipes object"""
    total = 0

    # Create an instance user input
    @staticmethod
    def userinstance():
        print("Creating a recipe instance")
        recepi_instance = input("What recepi name?")

        recepi_instance = Recipe(input("Enter your recipe Title: \n"), input("Enter your recipe ingredient: \n"), input("Enter your recipe instruction: \n"),input("Enter your recipe Type: \n") )

        return recepi_instance


    @staticmethod
    def status():
        print("\nThe total number of recepi is ", Recipes.total)
    def __init__(self, title, ingredient, instruction, type ):
        self.title = title
        self.ingredient = ingredient
        self.instruction = instruction
        self.type = type
        Recipe.total +=1


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






###############################################main##################

#global_recepi = Recepi_list()
#global_recepi.create_empty()
#title, description = global_recepi.add_recepi()
#global_recepi.show_recepi()

recepi1 = Recipe("Spagati", "Pasta, Tomato, Sauce, mince", "1:boil pasta\n2:do the sauce","dinner" )
recepi2 = Recipe("Oat Bowl", "Oat , Milk", "1: Put oat on stove\n2: pour milk in it \n3:wait until bubles", "Breakfast")
Recipe.userinstance()
print(recepi_instance)
print(recepi1)
print(recepi2)
Recipes.status()











