import random

class coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key, value in kwargs.items():
            setattr(self,key,value)
            
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value


        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour


    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        heads_options = [True , False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value > 1.00:
            return "{} Coin".format(int(self.original_value))
        else:
            return "{} Coin".format(int(self.original_value*100))   

    def __del__(self):
        print('Coin Spent!')
            

class one_rupee(coin):

    def __init__(self):
        data = {
                'original_value': 1.00,
                'clean_colour': 'silver',
                'rusty_colour': 'greenish',
                'num_edges': 1,
                'diameter':22.5,
                'thickness':2.15,
                'mass': 9.5,
               }

        super().__init__(**data)
    
class two_rupee(coin):

    def __init__(self):
        data = {
                'original_value': 2.00,
                'clean_colour': 'silver',
                'rusty_colour': 'greenish',
                'num_edges': 1,
                'diameter':32.5,
                'thickness':2.15,
                'mass': 12.5,
               }

        super().__init__(**data)
    
class five_rupee(coin):

    def __init__(self):
        data = {
                'original_value': 5.00,
                'clean_colour': 'silver',
                'rusty_colour': 'greenish',
                'num_edges': 1,
                'diameter':15.5,
                'thickness':4.15,
                'mass': 20.5,
               }

        super().__init__(**data)
    
class ten_rupee(coin):

    def __init__(self):
        data = {
                'original_value': 10.00,
                'clean_colour': 'Gold',
                'rusty_colour': None,
                'num_edges': 1,
                'diameter':15.5,
                'thickness':4.15,
                'mass': 20.5,
               }

        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour
            

coins = [
         one_rupee(),
         two_rupee(),
         five_rupee(),
         ten_rupee()
         ]

for coin in coins:
    arg = [
           coin,
           coin.colour,
           coin.value,
           coin.diameter,
           coin.thickness,
           coin.num_edges,
           coin.mass
          ]

    string = '{}-Colour:{}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}'.format(*arg)
