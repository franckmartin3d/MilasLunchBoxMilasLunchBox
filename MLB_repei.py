# Mila's lunchbox recepi feature


class Recepi_list(object):
    """Creating recepi dictionary"""
    #Create a empty dictionary
    def create_empty(self):
        """input:Nothing
        Output: 3 empty list"""

        global_recepi= {}
        breakfast_list = {}
        lunch_list = {}
        dinner_list = {}

        return global_recepi,lunch_list,dinner_list,breakfast_list

    #add new recepi to list
    def add_recepi(self):
        """input: nothing
        output: add a recepi"""
        # get the title of the recepei
        print("ADD A RECEPI")
        list = {}
        title = input("Recepi Title:")
        if title not in list:
            description = input("\n What is the descrition of the recepi:")
            list[title] = description
            print("\n", title, "Has been added.")
        else:
            print("the", title ," recepi is already in the list, try to edit it")
        return list

    def show_global_recepi(self, list):
        """show all recepi in global recepi"""
        print("Here are all your recepi")
        for key in list:
            print(key)

#main
list1 = Recepi_list()
list1.create_empty()
list1.add_recepi()
list1.show_global_recepi(list)










