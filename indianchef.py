from chef import Chef

class IndianChef(Chef):

    def make_samosa(self):
        print("Making Samosa")

my = IndianChef()

my.make_samosa()