# Menue system for lunchbox

class Menu(object):

    def __init__(self):
        self._options= {'a': self.optionA,
                        'b': self.optionB,
                        'c': self.optionC}

    def handle_option(self, option):
        if option not in self._options:
            print("Invalid Option")
            #re-draw
            return
        self._options[option]()


    def draw(self, option):


    def optionA(self):
        print("optionA")

