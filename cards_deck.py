from const import CARD_TYPE, SUITS
from models import Card
import random 

#contains all the deck of the cards possible  
class Deck:
    def __init__(self):
        self.deck = []

        for suit in SUITS:
           for card_type in CARD_TYPE:
              card= Card(card_type,suit)
              self.deck.append(card)

    def __repr__(self) -> str:
        return 'Deck of all the cards created'

    def random_set_of_three(self):
        random.shuffle(self.deck)
        return list(random.sample(self.deck,3))

