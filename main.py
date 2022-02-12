import random
from cards_deck import Deck
from game import Game
from helper import countOccurrencesInList, find_duplicates, rm_element_from_list
from models import Card
from const import SUITS,CARD_TYPE


game =Game()
game.welcome()
game.get_num_of_players()
game.get_names()
game.distribute_cards()
game.set_init_pool_amount()
game.start_betting()
game.show_results()

# card_list = [Card('6','Hearts'),Card('5','Spades'),Card('7','Diamond')]
# card_list = [Card('6','Hearts'),Card('6','Spades'),Card('6','Hearts')]
# val =game.check_for_pair(card_list)
# print(val)


# list = ['6','5','5','7','5']
# # x=find_duplicates(list)
# # print(x)
# print(rm_element_from_list(list,'5'))
