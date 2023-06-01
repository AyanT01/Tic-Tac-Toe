class Player:
    def __init__(self,type):
        self.type = type
        self.name = self.get_name()

    def get_name(self):
        if self.type == 'X':
            name = input("Player selecting X, what is your name? ")
        else:
            name = input("Player selecting O, what is your name? ")
        return name
