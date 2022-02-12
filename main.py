import random
from cards_deck import Deck
from models import Card
from const import SUITS,CARD_TYPE


deck =Deck()
for card in deck.random_set_of_three():
    print(card)