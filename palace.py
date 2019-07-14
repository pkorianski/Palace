# Imports
import random


# Main Class
class Palace:
    def __init__(self, num_players, player1, player2, player3, player4):
        self.num_players = num_players
        self.table_cards = []
        self.current_deck = []
        self.player1 = {
            "player_name": player1['name'],
            "isRobot": player1['isRobot'],
            "face_down_cards": [],
            "top_three_cards": [],
            "current_hand": []
        }
        self.player2 = {
            "player_name": player2['name'],
            "isRobot": player2['isRobot'],
            "face_down_cards": [],
            "top_three_cards": [],
            "current_hand": []
        }
        if num_players >= 3:
            self.player3 = {
                "player_name": player3['name'],
                "isRobot": player3['isRobot'],
                "face_down_cards": [],
                "top_three_cards": [],
                "current_hand": []
            }
        if num_players == 4:
            self.player4 = {
                "player_name": player4['name'],
                "isRobot": player4['isRobot'],
                "face_down_cards": [],
                "top_three_cards": [],
                "current_hand": []
            }

        self.deck_definition = {
            "2C": "go_again",
            "2H": "go_again",
            "2D": "go_again",
            "2S": "go_again",
            "3C": 3,
            "3H": 3,
            "3D": 3,
            "3S": 3,
            "4C": 4,
            "4H": 4,
            "4D": 4,
            "4S": 4,
            "5C": 5,
            "5H": 5,
            "5D": 5,
            "5S": 5,
            "6C": 6,
            "6H": 6,
            "6D": 6,
            "6S": 6,
            "7C": 7,
            "7H": 7,
            "7D": 7,
            "7S": 7,
            "8C": 8,
            "8H": 8,
            "8D": 8,
            "8S": 8,
            "9C": 9,
            "9H": 9,
            "9D": 9,
            "9S": 9,
            "10C": "clear_deck",
            "10H": "clear_deck",
            "10D": "clear_deck",
            "10S": "clear_deck",
            "JC": 11,
            "JH": 11,
            "JD": 11,
            "JS": 11,
            "QC": 12,
            "QH": 12,
            "QD": 12,
            "QS": 12,
            "KC": 13,
            "KH": 13,
            "KD": 13,
            "KS": 13,
            "AC": 14,
            "AH": 14,
            "AD": 14,
            "AS": 14,
        }

    def set_deck(self):
        if not self.current_deck:
            length_of_deck = len(self.deck_definition.keys())
            deck = ['']*length_of_deck
            current_indexes = [i for i in range(0, length_of_deck)]

            for card in self.deck_definition.keys():
                index = random.choice(current_indexes)
                current_indexes.remove(index)
                deck[index] = card
            self.current_deck = deck
        else:
            print('Deck is already shuffled')

    def get_deck(self):
        print(self.current_deck)

    def deal_cards(self):
        card_number = 0
        total_cards_dealt = (3*self.num_players) + (8*self.num_players)
        if self.num_players == 2:
            while card_number < total_cards_dealt:
                # Deal to Player1
                if len(self.player1['face_down_cards']) < 3:
                    self.player1['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player1['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]
                # Deal to Player2
                if len(self.player2['face_down_cards']) < 3:
                    self.player2['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player2['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]

                card_number += 2
            print('###### CONFIGURING DECK ######')
            self.deck_sort(self.player1)
            self.deck_sort(self.player2)
            print(f'Current size of deck: {len(self.current_deck)}')
            print(f'Player1: {self.player1}\n')
            print(f'Player2: {self.player2}\n')
            print('##############################\n')

        elif self.num_players == 3:
            while card_number < total_cards_dealt:
                # Deal to Player1
                if len(self.player1['face_down_cards']) < 3:
                    self.player1['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player1['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]
                # Deal to Player2
                if len(self.player2['face_down_cards']) < 3:
                    self.player2['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player2['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]
                # Deal to Player3
                if len(self.player3['face_down_cards']) < 3:
                    self.player3['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player3['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]

                card_number += 3
            print('###### CONFIGURING DECK ######')
            self.deck_sort(self.player1)
            self.deck_sort(self.player2)
            self.deck_sort(self.player2)
            print(f'Current size of deck: {len(self.current_deck)}')
            print(f'Player1: {self.player1}\n')
            print(f'Player2: {self.player2}\n')
            print(f'Player3: {self.player3}\n')
            print('##############################\n')

        elif self.num_players == 4:
            while card_number < total_cards_dealt:
                # Deal to Player1
                if len(self.player1['face_down_cards']) < 3:
                    self.player1['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player1['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]
                # Deal to Player2
                if len(self.player2['face_down_cards']) < 3:
                    self.player2['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player2['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]
                # Deal to Player3
                if len(self.player3['face_down_cards']) < 3:
                    self.player3['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player3['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]
                # Deal to Player4
                if len(self.player4['face_down_cards']) < 3:
                    self.player4['face_down_cards'].append(self.current_deck[0])
                    del self.current_deck[0]
                else:
                    self.player4['current_hand'].append(self.current_deck[0])
                    del self.current_deck[0]

                card_number += 4
            print('###### CONFIGURING DECK ######')
            self.deck_sort(self.player1)
            self.deck_sort(self.player2)
            self.deck_sort(self.player3)
            self.deck_sort(self.player4)
            print(f'Current size of deck: {len(self.current_deck)}')
            print(f'Player1: {self.player1}\n')
            print(f'Player2: {self.player2}\n')
            print(f'Player3: {self.player3}\n')
            print(f'Player3: {self.player4}\n')
            print('##############################\n')
        else:
            print('You cannot play Palace alone. Be social!')

    def pick_top_three_cards(self):
        print('###### PICKING TOP 3 CARDS ######')
        # Player1 (you)
        while True:
            card1 = input('Enter 1st top card: ')
            if card1 in self.player1['current_hand']:
                self.player1['top_three_cards'].append(card1)
                self.player1['current_hand'].remove(card1)
                break
            else:
                print(f'Invalid Card ({card1}). Try again.')
        while True:
            card2 = input('Enter 2nd top card: ')
            if card2 in self.player1['current_hand']:
                self.player1['top_three_cards'].append(card2)
                self.player1['current_hand'].remove(card2)
                break
            else:
                print(f'Invalid Card ({card2}). Try again.')
        while True:
            card3 = input('Enter 3rd top card: ')
            if card3 in self.player1['current_hand']:
                self.player1['top_three_cards'].append(card3)
                self.player1['current_hand'].remove(card3)
                break
            else:
                print(f'Invalid Card ({card3}). Try again.')
        print(self.player1)

        # Player2
        p2_current_hand_converted = [self.deck_definition[card] for card in self.player2['current_hand']]
        while True:
            if len(self.player2['top_three_cards']) < 3:
                if 'go_again' in p2_current_hand_converted:
                    for card in self.player2['current_hand']:
                        if self.deck_definition[card] == 'go_again':
                            self.player2['top_three_cards'].append(card)
                            self.player2['current_hand'].remove(card)
                    p2_current_hand_converted.remove('go_again')

                elif 'clear_deck' in p2_current_hand_converted:
                    for card in self.player2['current_hand']:
                        if self.deck_definition[card] == 'clear_deck':
                            self.player2['top_three_cards'].append(card)
                            self.player2['current_hand'].remove(card)
                    p2_current_hand_converted.remove('clear_deck')
                else:
                    p2_current_hand_converted.sort(reverse=True)
                    for card in self.player2['current_hand']:
                        if self.deck_definition[card] == p2_current_hand_converted[0]:
                            self.player2['top_three_cards'].append(card)
                            self.player2['current_hand'].remove(card)
                            del p2_current_hand_converted[0]
                            break
            else:
                break
        print(self.player2)
        print('##############################\n')

    def determine_starting_turn(self):
        print('###### DETERMINING STARTING TURN ######')
        # Player1 Hand
        player1_hand = [self.deck_definition[card] for card in self.player1['current_hand']
                        if card not in ["2C","2H","2D","2S","10C","10H","10D","10S"]]
        player1_hand.sort()

        # Player2 Hand
        player2_hand = [self.deck_definition[card] for card in self.player2['current_hand']
                        if card not in ["2C","2H","2D","2S","10C","10H","10D","10S"]]
        player2_hand.sort()

        print(f'Player1 lowest: {(player1_hand[0] if len(player1_hand) > 0 else "N/A")}')
        print(f'Player2 lowest: {(player2_hand[0] if len(player2_hand) > 0 else "N/A")}')
        print('##############################\n')

        if len(player1_hand) == 0:
            print('Player2 starts')
            for card in self.player2['current_hand']:
                if self.deck_definition[card] == player2_hand[0]:
                    print(f'Player2: Placed {card} onto table cards')
                    self.table_cards.append(card)
                    self.player2['current_hand'].remove(card)
                    break
            print(f'Player2: Picked up card {self.current_deck[0]}')
            self.player2['current_hand'].append(self.current_deck[0])
            self.current_deck = self.current_deck[1:]
            self.deck_sort(self.player2)
            print(self.player2)
            print(f'Table cards: {self.table_cards}')
            self.rounds(next_player='Player1')
        elif len(player2_hand) == 0:
            print('Player1 starts')
            for card in self.player1['current_hand']:
                if self.deck_definition[card] == player1_hand[0]:
                    print(f'Player1: Placed {card} onto table cards')
                    self.table_cards.append(card)
                    self.player1['current_hand'].remove(card)
                    break
            print(f'Player1: Picked up card {self.current_deck[0]}')
            self.player1['current_hand'].append(self.current_deck[0])
            self.current_deck = self.current_deck[1:]
            self.deck_sort(self.player1)
            print(self.player1)
            print(f'Table cards: {self.table_cards}')
            self.rounds(next_player='Player2')
        else:
            if player1_hand[0] < player2_hand[0]:
                print('Player1 starts')
                for card in self.player1['current_hand']:
                    if self.deck_definition[card] == player1_hand[0]:
                        print(f'Player1: Placed {card} onto table cards')
                        self.table_cards.append(card)
                        self.player1['current_hand'].remove(card)
                        break
                print(f'Player1: Picked up card {self.current_deck[0]}')
                self.player1['current_hand'].append(self.current_deck[0])
                self.current_deck = self.current_deck[1:]
                self.deck_sort(self.player1)
                print(self.player1)
                print(f'Table cards: {self.table_cards}')
                self.rounds(next_player='Player2')
            else:
                print('Player2 starts')
                for card in self.player2['current_hand']:
                    if self.deck_definition[card] == player2_hand[0]:
                        print(f'Player2: Placed {card} onto table cards')
                        self.table_cards.append(card)
                        self.player2['current_hand'].remove(card)
                        break
                print(f'Player2: Picked up card {self.current_deck[0]}')
                self.player2['current_hand'].append(self.current_deck[0])
                self.current_deck = self.current_deck[1:]
                self.deck_sort(self.player2)
                print(self.player2)
                print(f'Table cards: {self.table_cards}')
                self.rounds(next_player='Player1')

    def more_than_one_card(self, player, card_number, deck):
        for card in player[deck]:
            if card_number == self.deck_definition[card]:
                return True,card
        return False,None

    def did_player_win(self, player):
        # Winning selection
        if len(player['current_hand']) == 0 and len(player['top_three_cards']) == 0 and len(player['face_down_cards']) == 0 and len(self.current_deck) == 0:
           print(f'{player["player_name"]} has won Palace!')
           return True
        else:
           return False

    def deck_sort(self, player):
        if player == 'Player1':
            player = self.player1
        elif player == 'Player2':
            player = self.player2

        if len(player['current_hand']):
            new_deck = [[self.deck_definition[c], c] for c in player['current_hand'] if self.deck_definition[c] != 'go_again' and
                        self.deck_definition[c] != 'clear_deck']

            wild_cards = [c for c in player['current_hand'] if self.deck_definition[c] == 'go_again' or
                          self.deck_definition[c] == 'clear_deck']

            new_deck = sorted(new_deck, key=lambda x: x[0])

            new_deck = [c[1] for c in new_deck]
            new_deck.extend(wild_cards)
            player['current_hand'] = new_deck

    def rounds(self, next_player):
        turn = next_player
        while True:
            if turn == 'Player1':
                self.deck_sort(self.player1)
                decision = input('Do you have to pickup (y/n)?: ')

                if (decision.lower() == 'y' or decision.lower() == 'yes') and len(self.table_cards):
                    self.player1['current_hand'].extend(self.table_cards)
                    self.table_cards = []
                    print(self.table_cards)
                    print(self.player1)
                    turn = 'Player2'

                elif decision.lower() == 'n' or decision.lower() == 'no':
                    loops = 0
                    old_card = ""
                    while True:
                        self.deck_sort(self.player1)
                        card_in_hand = True
                        if loops == 0:
                            card = input('Play next card: Type "exit" if mistaken: ')
                            if card.lower() == 'exit':
                                break

                            old_card = card
                        if loops > 0:
                            while True:
                                print(self.player1)
                                card = input('Play next card. Type "done" if finished duplicate cards: ')
                                if card.lower() == 'done':
                                    break
                                elif card in self.deck_definition.keys() and self.deck_definition[card] != self.deck_definition[old_card]\
                                        and self.deck_definition[old_card] != 'clear_deck' and self.deck_definition[old_card] != 'go_again':
                                    print('Try again. The card is not the same number.')
                                    continue
                                elif card in self.deck_definition.keys() and (self.deck_definition[card] == self.deck_definition[old_card]
                                        or (self.deck_definition[old_card] == 'clear_deck' or self.deck_definition[old_card] == 'go_again') ):
                                    break
                            if card.lower() == 'done':
                                break

                        # No cards are in the table set. Place any new card
                        if card in self.deck_definition.keys() and len(self.table_cards) == 0:

                            if card in self.player1['current_hand']:
                                # GO
                                if self.deck_definition[card] == 'go_again':
                                    print('Player1 got a go_again')
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['current_hand'].remove(card)
                                    if len(self.current_deck) > 0 and len(self.player1['current_hand']) < 5:
                                        self.player1['current_hand'].append(self.current_deck[0])
                                        del self.current_deck[0]
                                        print(self.player1)
                                    else:
                                        if self.did_player_win(self.player1):
                                            return

                                elif self.deck_definition[card] == 'clear_deck':
                                    print('Player1 got a clear_deck')
                                    self.table_cards = []
                                    print(self.table_cards)
                                    self.player1['current_hand'].remove(card)
                                    if len(self.current_deck) > 0 and len(self.player1['current_hand']) < 5:
                                        self.player1['current_hand'].append(self.current_deck[0])
                                        del self.current_deck[0]
                                        print(self.player1)
                                    else:
                                        if self.did_player_win(self.player1):
                                            return

                                else:
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['current_hand'].remove(card)
                                    if len(self.current_deck) > 0 and len(self.player1['current_hand']) < 5:
                                        self.player1['current_hand'].append(self.current_deck[0])
                                        del self.current_deck[0]
                                        print(self.player1)
                                    else:
                                        if self.did_player_win(self.player1):
                                            return
                                    turn = 'Player2'
                            elif card in self.player1['top_three_cards'] and len(
                                    self.player1['current_hand']) == 0:
                                # GO
                                if self.deck_definition[card] == 'go_again':
                                    print('Player1 got a go_again')
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['top_three_cards'].remove(card)
                                    print(self.player1)

                                elif self.deck_definition[card] == 'clear_deck':
                                    print('Player1 got a clear_deck')
                                    self.table_cards = []
                                    print(self.table_cards)
                                    self.player1['top_three_cards'].remove(card)
                                    print(self.player1)

                                else:
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['top_three_cards'].remove(card)
                                    turn = 'Player2'
                                    print(self.player1)

                            elif card in self.player1['face_down_cards'] and len(
                                    self.player1['top_three_cards']) == 0 and len(
                                    self.player1['current_hand']) == 0:
                                # GO
                                if self.deck_definition[card] == 'go_again':
                                    print('Player1 got a go_again')
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['face_down_cards'].remove(card)
                                    print(self.player1)
                                    if self.did_player_win(self.player1):
                                        return

                                elif self.deck_definition[card] == 'clear_deck':
                                    print('Player1 got a clear_deck')
                                    self.table_cards = []
                                    print(self.table_cards)
                                    self.player1['face_down_cards'].remove(card)
                                    print(self.player1)
                                    if self.did_player_win(self.player1):
                                        return

                                else:
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['face_down_cards'].remove(card)
                                    print(self.player1)
                                    if self.did_player_win(self.player1):
                                        return
                                    turn = 'Player2'
                            else:
                                print(f'{self.player1["player_name"]} typed incorrect card ({card}). Try again.')
                                card_in_hand = False

                        elif card in self.deck_definition.keys() and len(self.table_cards) > 0:
                            print('Player1 playing')
                            if card in self.player1['current_hand']:
                                if self.deck_definition[card] == 'go_again':
                                    print('Player1 got a go_again')
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['current_hand'].remove(card)
                                    print(self.player1)
                                    if len(self.current_deck) > 0 and len(self.player1['current_hand']) < 5:
                                        self.player1['current_hand'].append(self.current_deck[0])
                                        del self.current_deck[0]
                                        print(self.player1)
                                    else:
                                        if self.did_player_win(self.player1):
                                            return

                                elif self.deck_definition[card] == 'clear_deck':
                                    print('Player1 got a clear_deck')
                                    self.table_cards = []
                                    print(self.table_cards)
                                    self.player1['current_hand'].remove(card)
                                    print(self.player1)
                                    if len(self.current_deck) > 0 and len(self.player1['current_hand']) < 5:
                                        self.player1['current_hand'].append(self.current_deck[0])
                                        del self.current_deck[0]
                                        print(self.player1)
                                    else:
                                        if self.did_player_win(self.player1):
                                            return

                                elif self.deck_definition[self.table_cards[0]] == 'go_again':
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['current_hand'].remove(card)
                                    print(self.player1)
                                    if len(self.current_deck) > 0 and len(self.player1['current_hand']) < 5:
                                        self.player1['current_hand'].append(self.current_deck[0])
                                        del self.current_deck[0]
                                        print(self.player1)
                                    else:
                                        if self.did_player_win(self.player1):
                                            return
                                    turn = 'Player2'

                                elif self.deck_definition[card] >= self.deck_definition[self.table_cards[0]]:
                                    # GO
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['current_hand'].remove(card)
                                    print(self.player1)
                                    if len(self.current_deck) > 0 and len(self.player1['current_hand']) < 5:
                                        self.player1['current_hand'].append(self.current_deck[0])
                                        del self.current_deck[0]
                                        print(self.player1)
                                    else:
                                        if self.did_player_win(self.player1):
                                            return
                                    turn = 'Player2'

                            elif card in self.player1['top_three_cards'] and len(self.player1['current_hand']) == 0:

                                if self.deck_definition[card] == 'go_again':
                                    print('Player1 got a go_again')
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['top_three_cards'].remove(card)
                                    print(self.player1)

                                elif self.deck_definition[card] == 'clear_deck':
                                    print('Player1 got a clear_deck')
                                    self.table_cards = []
                                    print(self.table_cards)
                                    self.player1['top_three_cards'].remove(card)
                                    print(self.player1)

                                elif self.deck_definition[self.table_cards[0]] == 'go_again':
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['top_three_cards'].remove(card)
                                    print(self.player1)
                                    turn = 'Player2'

                                elif self.deck_definition[card] >= self.deck_definition[self.table_cards[0]]:
                                    # GO
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['top_three_cards'].remove(card)
                                    print(self.player1)
                                    turn = 'Player2'

                            elif card in self.player1['face_down_cards'] and len(
                                    self.player1['top_three_cards']) == 0 and len(self.player1['current_hand']) == 0:
                                if self.deck_definition[card] == 'go_again':
                                    print('Player1 got a go_again')
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['face_down_cards'].remove(card)
                                    print(self.player1)
                                    if self.did_player_win(self.player1):
                                        return

                                elif self.deck_definition[card] == 'clear_deck':
                                    print('Player1 got a clear_deck')
                                    self.table_cards = []
                                    print(self.table_cards)
                                    self.player1['face_down_cards'].remove(card)
                                    print(self.player1)
                                    if self.did_player_win(self.player1):
                                        return

                                elif self.deck_definition[self.table_cards[0]] == 'go_again':
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['face_down_cards'].remove(card)
                                    print(self.player1)
                                    if self.did_player_win(self.player1):
                                        return
                                    turn = 'Player2'

                                elif self.deck_definition[card] >= self.deck_definition[self.table_cards[0]]:
                                    # GO
                                    self.table_cards.insert(0, card)
                                    print(self.table_cards)
                                    self.player1['face_down_cards'].remove(card)
                                    print(self.player1)
                                    if self.did_player_win(self.player1):
                                        return
                                    turn = 'Player2'
                            else:
                                print(f'{self.player1["player_name"]} typed incorrect card ({card}). Try again.')
                                card_in_hand = False

                        if card in self.deck_definition.keys() and card_in_hand:
                            loops += 1
                else:
                    print(f'{self.player1["player_name"]} typed incorrect card ({card}). Try again.')

            elif turn == 'Player2':
                self.deck_sort(turn)
                print('Player2s turn')

                if len(self.player2['current_hand']):
                    # Get normal numbered cards
                    print('Player2 in current_hand')
                    sorted_hand = [(self.deck_definition[card], card) for card in self.player2['current_hand']
                                   if card not in ["2C", "2H", "2D", "2S", "10C", "10H", "10D", "10S"]]

                    if len(sorted_hand) > 0:
                        sorted_hand = sorted(sorted_hand, key=lambda x: x[0])

                    # Get wildcard cards
                    for wc in ["2C", "2H", "2D", "2S", "10C", "10H", "10D", "10S"]:
                        if wc in self.player2['current_hand']:
                            sorted_hand.append((self.deck_definition[wc], wc))

                    # Go through deck to see if Player2 can put down a card
                    pick_up_table_cards = True
                    for i, card_tup in enumerate(sorted_hand):
                        card = card_tup[1]

                        if len(self.table_cards) == 0:

                            if card_tup[0] == 'go_again':
                                print('Player2 got a go_again')
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['current_hand'].remove(card)
                                print(self.player2)
                                if len(self.current_deck) > 0 and len(self.player2['current_hand']) < 5:
                                    self.player2['current_hand'].append(self.current_deck[0])
                                    del self.current_deck[0]
                                    print(self.player2)
                                else:
                                    if self.did_player_win(self.player2):
                                        return
                                pick_up_table_cards = False
                                break

                            elif card_tup[0] == 'clear_deck':
                                print('Player2 got a clear_deck')
                                self.table_cards = []
                                print(self.table_cards)
                                self.player2['current_hand'].remove(card)
                                print(self.player2)
                                if len(self.current_deck) > 0 and len(self.player2['current_hand']) < 5:
                                    self.player2['current_hand'].append(self.current_deck[0])
                                    del self.current_deck[0]
                                    print(self.player2)
                                else:
                                    if self.did_player_win(self.player2):
                                        return
                                pick_up_table_cards = False
                                break

                            else:
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['current_hand'].remove(card)
                                print(self.player2)
                                if len(self.current_deck) > 0 and len(self.player2['current_hand']) < 5:
                                    self.player2['current_hand'].append(self.current_deck[0])
                                    del self.current_deck[0]
                                    print(self.player2)
                                else:
                                    if self.did_player_win(self.player2):
                                        return
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break

                        elif len(self.table_cards) > 0:

                            if card_tup[0] == 'go_again':
                                print('Player2 got a go_again')
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['current_hand'].remove(card)
                                print(self.player2)
                                if len(self.current_deck) > 0 and len(self.player2['current_hand']) < 5:
                                    self.player2['current_hand'].append(self.current_deck[0])
                                    del self.current_deck[0]
                                    print(self.player2)
                                else:
                                    if self.did_player_win(self.player2):
                                        return
                                pick_up_table_cards = False
                                break

                            elif card_tup[0] == 'clear_deck':
                                print('Player2 got a clear_deck')
                                self.table_cards = []
                                print(self.table_cards)
                                self.player2['current_hand'].remove(card)
                                print(self.player2)
                                if len(self.current_deck) > 0 and len(self.player2['current_hand']) < 5:
                                    self.player2['current_hand'].append(self.current_deck[0])
                                    del self.current_deck[0]
                                    print(self.player2)
                                else:
                                    if self.did_player_win(self.player2):
                                        return
                                pick_up_table_cards = False
                                break

                            elif self.deck_definition[self.table_cards[0]] == 'go_again':
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['current_hand'].remove(card)
                                print(self.player2)
                                if len(self.current_deck) > 0 and len(self.player2['current_hand']) < 5:
                                    self.player2['current_hand'].append(self.current_deck[0])
                                    del self.current_deck[0]
                                    print(self.player2)
                                else:
                                    if self.did_player_win(self.player2):
                                        return
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break

                            elif self.deck_definition[card] >= self.deck_definition[self.table_cards[0]]:
                                # GO
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['current_hand'].remove(card)
                                print(self.player2)
                                if len(self.current_deck) > 0 and len(self.player2['current_hand']) < 5:
                                    self.player2['current_hand'].append(self.current_deck[0])
                                    del self.current_deck[0]
                                    print(self.player2)
                                else:
                                    if self.did_player_win(self.player2):
                                        return
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break


                    # No available cards to put down. Pick up cards
                    if pick_up_table_cards:
                        self.player2['current_hand'].extend(self.table_cards)
                        self.table_cards = []
                        print(self.table_cards)
                        print('Player2 picks up table cards')
                        print(self.player2)
                        turn = 'Player1'

                elif len(self.player2['top_three_cards']):
                    # Get normal numbered cards
                    print('Player2 in top_three_cards')
                    sorted_hand = [(self.deck_definition[card], card) for card in self.player2['top_three_cards']
                                   if card not in ["2C", "2H", "2D", "2S", "10C", "10H", "10D", "10S"]]

                    if len(sorted_hand) > 0:
                        sorted_hand = sorted(sorted_hand, key=lambda x: x[0])

                    # Get wildcard cards
                    for wc in ["2C", "2H", "2D", "2S", "10C", "10H", "10D", "10S"]:
                        if wc in self.player2['top_three_cards']:
                            sorted_hand.append((self.deck_definition[wc], wc))

                    # Go through deck to see if Player2 can put down a card
                    pick_up_table_cards = True
                    for i, card_tup in enumerate(sorted_hand):
                        card = card_tup[1]

                        if len(self.table_cards) == 0:

                            if card_tup[0] == 'go_again':
                                print('Player2 got a go_again')
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['top_three_cards'].remove(card)
                                print(self.player2)
                                pick_up_table_cards = False
                                break

                            elif card_tup[0] == 'clear_deck':
                                print('Player2 got a clear_deck')
                                self.table_cards = []
                                print(self.table_cards)
                                self.player2['top_three_cards'].remove(card)
                                print(self.player2)
                                pick_up_table_cards = False
                                break

                            else:
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['top_three_cards'].remove(card)
                                print(self.player2)
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break

                        elif len(self.table_cards) > 0:

                            if card_tup[0] == 'go_again':
                                print('Player2 got a go_again')
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['top_three_cards'].remove(card)
                                print(self.player2)
                                pick_up_table_cards = False
                                break

                            elif card_tup[0] == 'clear_deck':
                                print('Player2 got a clear_deck')
                                self.table_cards = []
                                print(self.table_cards)
                                self.player2['top_three_cards'].remove(card)
                                print(self.player2)
                                pick_up_table_cards = False
                                break

                            elif self.deck_definition[self.table_cards[0]] == 'go_again':
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['top_three_cards'].remove(card)
                                print(self.player2)
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break

                            elif self.deck_definition[card] >= self.deck_definition[self.table_cards[0]]:
                                # GO
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['top_three_cards'].remove(card)
                                print(self.player2)
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break

                    # No available cards to put down. Pick up cards
                    if pick_up_table_cards:
                        self.player2['current_hand'].extend(self.table_cards)
                        self.table_cards = []
                        print(self.table_cards)
                        print('Player2 picks up table cards')
                        print(self.player2)
                        turn = 'Player1'

                elif len(self.player2['face_down_cards']):
                    # Get normal numbered cards
                    print('Player2 in face_down_cards')
                    sorted_hand = [(self.deck_definition[card], card) for card in self.player2['face_down_cards']
                                   if card not in ["2C", "2H", "2D", "2S", "10C", "10H", "10D", "10S"]]

                    if len(sorted_hand) > 0:
                        sorted_hand = sorted(sorted_hand, key=lambda x: x[0])

                    # Get wildcard cards
                    for wc in ["2C", "2H", "2D", "2S", "10C", "10H", "10D", "10S"]:
                        if wc in self.player2['face_down_cards']:
                            sorted_hand.append((self.deck_definition[wc], wc))

                    # Go through deck to see if Player2 can put down a card
                    pick_up_table_cards = True
                    for i, card_tup in enumerate(sorted_hand):
                        card = card_tup[1]

                        if len(self.table_cards) == 0:

                            if card_tup[0] == 'go_again':
                                print('Player2 got a go_again')
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['face_down_cards'].remove(card)
                                print(self.player2)
                                if self.did_player_win(self.player2):
                                    return
                                pick_up_table_cards = False
                                break

                            elif card_tup[0] == 'clear_deck':
                                print('Player2 got a clear_deck')
                                self.table_cards = []
                                print(self.table_cards)
                                self.player2['face_down_cards'].remove(card)
                                print(self.player2)
                                if self.did_player_win(self.player2):
                                    return
                                pick_up_table_cards = False
                                break

                            else:
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['face_down_cards'].remove(card)
                                print(self.player2)
                                if self.did_player_win(self.player2):
                                    return
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break

                        elif len(self.table_cards) > 0:

                            if card_tup[0] == 'go_again':
                                print('Player2 got a go_again')
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['face_down_cards'].remove(card)
                                print(self.player2)
                                if self.did_player_win(self.player2):
                                    return
                                pick_up_table_cards = False
                                break

                            elif card_tup[0] == 'clear_deck':
                                print('Player2 got a clear_deck')
                                self.table_cards = []
                                print(self.table_cards)
                                self.player2['face_down_cards'].remove(card)
                                print(self.player2)
                                if self.did_player_win(self.player2):
                                    return
                                pick_up_table_cards = False
                                break

                            elif self.deck_definition[self.table_cards[0]] == 'go_again':
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['face_down_cards'].remove(card)
                                print(self.player2)
                                if self.did_player_win(self.player2):
                                    return
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break

                            elif self.deck_definition[card] >= self.deck_definition[self.table_cards[0]]:
                                # GO
                                self.table_cards.insert(0, card)
                                print(self.table_cards)
                                self.player2['face_down_cards'].remove(card)
                                print(self.player2)
                                if self.did_player_win(self.player2):
                                    return
                                turn = 'Player1'
                                pick_up_table_cards = False
                                break

                    # No available cards to put down. Pick up cards
                    if pick_up_table_cards:
                        self.player2['current_hand'].extend(self.table_cards)
                        self.table_cards = []
                        print(self.table_cards)
                        print('Player2 picks up table cards')
                        print(self.player2)
                        turn = 'Player1'


def play_game(players, player1, player2, player3=None, player4=None):
    palace = Palace(players, player1=player1, player2=player2,
                    player3_name=player3, player4_name=player4)
    palace.set_deck()
    palace.deal_cards()
    palace.pick_top_three_cards()
    palace.determine_starting_turn()


# Run
if __name__ == '__main__':
    play_game(players=4, player1={'name':'Patrick', 'isRobot': 'n'},
                         player2={'name': 'Robocop', 'isRobot': 'y'},
                         player3={'name': 'Arod', 'isRobot': 'y'},
                         player4={'name': 'DJ', 'isRobot': 'y'})





#
