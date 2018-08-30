# Lunch Box creator


# -----------------------------------------> CLASS <--------------------------------------------------------------------


#Item class




class LunchItem(object):
    """Creating items object to use by the lunchbox"""
    item = 0

# list of instance objects
    itemlist = []


#Attribute of the class , Title, Nutitious value, type

    def __init__(self, title, nvalue, type):
        self.title = title
        self.nvalue = float(nvalue)
        self.type = type
        LunchItem.total +=1

    # Add to itemlist
        LunchItem.itemlist.append(self)

# Display the object when using print
    def __str__(self):
        rep = str.upper(self.title) + '\n\n'
        rep += str.rep += "Nutitious Value: \n" + self.nvalue + " \n\n"
        rep += "type: \n" + self.type + " \n\n"