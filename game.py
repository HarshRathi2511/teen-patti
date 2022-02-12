from cards_deck import Deck
from models import Player


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

    def get_names(self):
        try:
            # int objects are not iterable fix by using range
            for index in range(Game.num_of_players):
                player_name = input(f'Enter name of player no. {index+1}:  ')
                self.players.append(Player(player_name))

        except ValueError:
            print('Enter a valid name')

    def distribute_cards(self):
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

        if len(values_list) < 1:
            return False
        min_val = min(values_list)
        max_val = max(values_list)
        if max_val - min_val + 1 == len(values_list):
            for i in range(len(values_list)):
                if values_list[i] < 0:
                    j = -values_list[i] - min_val
                else:
                    j = values_list[i] - min_val
                    if values_list[j] > 0:
                        values_list[j] = -values_list[j]
                    else:
                        return False
                return True
        return False

    @staticmethod
    def check_for_pure_sequence(card_list):

        # check for the same suit
        if card_list[0].suit == card_list[1].suit == card_list[2].suit:
            # then check for sequence
            if_sequence = Game.check_for_sequence(card_list)
            return if_sequence
        else:
            return False

    @staticmethod  #all cards of the same suit
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
            
            print(player.sum_of_cards) 

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

            else: #if all the above fail then push to high card
                players_with_high_card.append(player)

        print(players_with_trail )
        print(players_with_pure_sequence)
        print(players_with_sequence)
        print(players_with_color)
        print(players_with_pair)
        print(players_with_high_card)     
                            
                            

        
        