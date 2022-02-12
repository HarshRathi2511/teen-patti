from cards_deck import Deck
from helper import countOccurrencesInList, find_duplicates, rm_element_from_list
from models import Player
import time


class Game:

    num_of_players = 0

    def __init__(self):
        self.players = []
        self.deck = Deck()

    @staticmethod
    def welcome():
        print('Welcome to Teen Patti hosted by Harsh Rathi\n')
        print('Rules of the game: \n 3 cards distributed to each player\n')
        print('Hierarchy of cards')
        print(
            """
1. Trails
2. Pure Sequence or Straight Flush
3. Sequence or Run
4. Color
5. Pair
6. High Card
        """
        )

    def get_num_of_players(self):
        try:
            Game.num_of_players = int(input('Enter the number of players !'))

            if Game.num_of_players <= 1:
                print(
                    f'Minimum two players are required to start this game instead of {Game.num_of_players}\n')
                print('Enter number of players again:-')
                exit()

        except ValueError:
            print('Couldn\'t understand it !')
            exit()

    def get_names(self):
        try:
            # int objects are not iterable fix by using range
            for index in range(Game.num_of_players):
                player_name = input(f'Enter name of player no. {index+1}:  ')
                self.players.append(Player(player_name))

        except ValueError:
            print('Enter a valid name')
            exit()

    def distribute_cards(self):
        print('Distributing cards......')
        time.sleep(1)
        for player in self.players:
            player.cards = self.deck.random_set_of_three()

            print(f'{player.name} has')
            for card in player.cards:
                print('{} of {}'.format(card.card_type, card.suit))

            print('..................')

    @staticmethod  # returns true if three of a kind
    def check_for_trail(card_list):
        if card_list[0].card_type == card_list[1].card_type == card_list[2].card_type:
            print('It is a three of kind')
            return True

    @staticmethod
    def check_for_sequence(card_list):
        values_list = []
        for card in card_list:
            values_list.append(card.value)

        # if len(values_list) < 1:
        #     return False
        # min_val = min(values_list)
        # max_val = max(values_list)
        # if max_val - min_val + 1 == len(values_list):
        #     for i in range(len(values_list)):
        #         if values_list[i] < 0:
        #             j = -values_list[i] - min_val
        #         else:
        #             j = values_list[i] - min_val
        #             if values_list[j] > 0:
        #                 values_list[j] = -values_list[j]
        #             else:
        #                 return False
        #         return True
        # return False
        
        return sorted(values_list) == list(range(min(values_list), max(values_list)+1))

    @staticmethod
    def check_for_pure_sequence(card_list):

        # check for the same suit
        if card_list[0].suit == card_list[1].suit == card_list[2].suit:
            # then check for sequence
            if_sequence = Game.check_for_sequence(card_list)
            return if_sequence
        else:
            return False

    @staticmethod  # all cards of the same suit
    def check_for_flush(card_list):
        if card_list[0].suit == card_list[1].suit == card_list[2].suit:
            return True
        else:
            return False

    @staticmethod
    def check_for_pair(card_list):
        values_list = [card.value for card in card_list]

        if values_list[0] == values_list[1] and values_list[1] != values_list[2]:
            return True
        if values_list[1] == values_list[2] and values_list[1] != values_list[0]:
            return True
        if values_list[0] == values_list[2] and values_list[0] != values_list[1]:
            return True
        return False

    def start_game(self):
        players_with_trail = []
        players_with_pure_sequence = []
        players_with_sequence = []
        players_with_color = []
        players_with_pair = []
        players_with_high_card = []

        for player in self.players:

            # print(player.sum_of_cards)

            if self.check_for_trail(player.cards):
                players_with_trail.append(player)

            elif self.check_for_pure_sequence(player.cards):
                players_with_pure_sequence.append(player)

            elif self.check_for_sequence(player.cards):
                players_with_sequence.append(player)

            elif self.check_for_flush(player.cards):
                players_with_color.append(player)

            elif self.check_for_pair(player.cards):
                players_with_pair.append(player)

            else:  # if all the above fail then push to high card
                players_with_high_card.append(player)

        print(players_with_trail)
        print(players_with_pure_sequence)
        print(players_with_sequence)
        print(players_with_color)
        print(players_with_pair)
        
        print(players_with_high_card)

        if players_with_trail:
            sum_list = []
            for player in players_with_trail:
                print(f'{player.name} has a trail set(three of a kind)')
                sum_list.append(player.sum_of_cards)

            # only one possible max value
            max_value = max(sum_list)

            for player in players_with_trail:
                if player.sum_of_cards == max_value:
                    # Game.winner = player
                    print(f'Game won by {player.name} due to trail')
                    exit()

        if players_with_pure_sequence:
            sum_list = []
            for player in players_with_pure_sequence:
                print(f'{player.name} has a pure sequence')
                sum_list.append(player.sum_of_cards)

            max_value = max(sum_list)

            count = countOccurrencesInList(sum_list, max_value)

            if count == 1:  # there is only one set of cards which has max value
                # to find that player who has max occurence
                for player in players_with_pure_sequence:
                    if player.sum_of_cards == max_value:
                        # Game.winner = player
                        print(
                            f'Game won by {player.name} due to pure sequence')
                        exit()

        if players_with_sequence:
            sum_list = []
            for player in players_with_sequence:
                print(f'{player.name} has a straight (non pure sequence)')
                sum_list.append(player.sum_of_cards)

            max_value = max(sum_list)

            count = countOccurrencesInList(sum_list, max_value)

            if count == 1:
                for player in players_with_sequence:
                    if player.sum_of_cards == max_value:
                        # Game.winner = player
                        print(f'Game won by {player.name} due to sequence ')
                        exit()

        if players_with_color:
            sum_list = []
            for player in players_with_color:
                print(f'{player.name} has a flush') 
                sum_list.append(player.sum_of_cards) 

            max_value = max(sum_list)

            # count = countOccurrencesInList(sum_list, max_value)

            # if a case between two flush then the deck with highest card wins
            no_of_flush = len(players_with_color)

            if no_of_flush == 1:
                for player in players_with_color:
                      
                    if player.sum_of_cards == max_value:
                        # Game.winner = player
                        print(f'Game won by {player.name} due to flush')
                        exit()

            else:
                # it is a draw so check for maximum card
                max_card_list = []
                for player in players_with_color:
                    max_card_list.append(player.max_card_value)

                for player in players_with_color:
                    if player.max_card_value == max(max_card_list):
                        # Game.winner = player
                        print(f'Game won by {player.name} due to flush')
                        exit()

        if players_with_pair:
            # no_of_players_with_pair= len
            pair_list = []  # contains the pair card value of each player
            for player in players_with_pair:
                print(f'{player.name} has a pair')  
                card_values = [card.value for card in player.cards]
                pair_element = find_duplicates(card_values)[0]
                pair_list.append(pair_element)
             

            max_value = max(pair_list)

            count_of_max = countOccurrencesInList(pair_list, max_value)

            if count_of_max==1:
                for player in players_with_pair:
                    card_value_set = [ card.value for card in player.cards]
                    card_pair_value= find_duplicates(card_value_set)

                    if card_pair_value[0] == max_value:
                        # Game.winner = player
                        print(
                            f'Game won by {player.name} due to pair')
                        exit()  


            else:
            # # if the pair card is of equal weights then check for the third card
            # # this could be done by simply comparing sum of cards
                third_card_values = []
                for player in players_with_pair:
                    # delete the max value from the card deck of each to get the third element
                    card_values = [card.value for card in player.cards]
                    third_card = rm_element_from_list(
                        card_values, max_value)[0]
                    player.third_card_value = third_card
                    third_card_values.append(third_card)
                    print(third_card_values)
                    for player in players_with_pair:
                      if player.third_card_value == max(third_card_values):
                        # Game.winner = player
                        print(
                            f'Game won by {player.name} due to draw of pair cards and third card greater')
                        exit() 



        if players_with_high_card:
            max_high_card_list=[]
            for player in players_with_high_card:
                print(f'{player.name} don\'t have above patterns')
                card_values= [ card.value for card in player.cards]  
                max_high_card_list.append(max(card_values))

            print(max_high_card_list)    
            max_value = max(max_high_card_list)
            # print(max_value)

            count_of_max = countOccurrencesInList(max_high_card_list,max_value)
            # print(f'Count of max {count_of_max}')

            # if count_of_max==1:
            winner_list=[]
            for player in players_with_high_card:
                    # print(player.max_card_value)
                    if player.max_card_value==max_value:
                        # Game.winner = player
                        winner_list.append(player.name)
                        print(
                            f'Game won by {player.name} due to having a bigger high card')

            if len(winner_list)>1:
                print(f'Draw between :-{winner_list}')
                            
                        
            exit() 



