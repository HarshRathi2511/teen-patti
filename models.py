from const import VALUES

class Player:
    def __init__(self, name):
        self.name = name
        self.cards= []

    def __str__(self):
        return self.name +' has the cards ' + self.cards   


class Card:
    def __init__(self,card_type,suit): 
        self.card_type = card_type
        self.suit = suit
        self.value = VALUES[card_type]

    def __str__(self):
        return self.card_type + ' of ' + self.suit  