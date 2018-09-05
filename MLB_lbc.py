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
    fruilist = []
    dairylist =[]




#Attribute of the class , Title, Nutitious value, type

    def __init__(self, title, nvalue, type):
        self.title = title
        self.nvalue = int(nvalue)
        self.type = type
        LunchItem.total +=1

    # Add to itemlist
        LunchItem.itemlist.append(self)

        if self.type == "mael" or self == "Meal":
            LunchItem.meallist.append(self)



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
    for i, val in enumerate(Recipe.rlist):
        print("\t", i, val.title)
