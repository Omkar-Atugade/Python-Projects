import random

class Rupees:

    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.value = 1.00
        self.colour = 'silver'
        self.num_edges = 1
        self.tickness = 3.15
        self.diameter = 22.15
        self.heads = True


    def rust(self):
        self.colour = 'gold'

    def clean(self):
        self.colour = 'silver'

    def flip(self):
        heads_options = [True , False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print('Coin Spent!')
        

        

