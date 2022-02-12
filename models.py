from django.forms import ValidationError
from const import VALUES

class Player:
    def __init__(self, name):
        self.name = name
        self.cards= []

    def __str__(self):
        card_name=[]
        for card in self.cards:
            card_name.append(card.__str__())
           
        return self.name +' has the cards ' + str(card_name)  
        
    def display_cards(self):
        print(f'{self.name} has')
        for card in self.cards:               
                print('{} of {}'.format(card.card_type,card.suit)) 
    
    @property  #now it can be accessed using player.sum_of_cards
    def sum_of_cards(self):
        value=0
        for card in self.cards:
            value = value+ card.value
        return value   

    @property
    def max_card_value(self):
        value=[]
        for card in self.cards:
            value.append(card.value) 
        return max(value)  

    def raise_amount(self):
        try:
            print(f'Player {self.name}')
            amount= input('Raise amount by:-  ')
            return amount

        except ValidationError:
            print('Couldn\'t understand')
            exit() 

    def fold_cards(self):
        try:
            print(f'Player {self.name}')
            isFold= input('Are you sure to fold type (Y/N):-  ')
            if isFold=='Y' or isFold=='y':
                return True
            else:
                return False    

        except ValidationError:
            print('Couldn\'t understand')
            exit()
                
                    




class Card:
    def __init__(self,card_type,suit): 
        self.card_type = card_type
        self.suit = suit
        self.value = VALUES[card_type]

    def __str__(self):
        return self.card_type + ' of ' + self.suit  

        