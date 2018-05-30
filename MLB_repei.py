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


#main
global_recepi = Recepi_list()

#global_recepi, breakfast_list, lunch_list, dinner_list = list1.create_empty()
global_recepi.create_empty()
title, description = global_recepi.add_recepi()
global_recepi.show_recepi()










