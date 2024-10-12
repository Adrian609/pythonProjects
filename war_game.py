import random

def build_deck():
    suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
    values = list(range(2, 15))    # 2-10, J, Q, K, A (where A=14)
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def build_hand(card_deck):
    hand=[]
    for i in range(0, 14):
        hand.append(card_deck[i])
        deck.pop(i)
    return hand

def play_game(player_one_hand, player_two_hand):
    player_one_wins = 0
    player_two_wins = 0
    for i in range(0, len(player_one_hand)):
        if player_one_hand[i] > player_two_hand[i]:
            player_one_wins += 1
            print(f"{player_one_hand[i]} {player_two_hand[i]} player one wins {player_one_wins} : {player_two_wins}")

        elif player_two_hand[i] > player_one_hand[i]:
            player_two_wins += 1
            print(f"{player_one_hand[i]} + {player_two_hand[i]} player two wins {player_one_wins} : {player_two_wins}")


    if player_one_wins > player_two_wins:
        return f"player_one_wins {player_one_wins} : {player_two_wins}"
    elif player_two_wins == player_one_wins:
        return f"Tie {player_two_wins} : {player_one_wins}"
    return f"player_two_wins {player_two_wins} : {player_one_wins}"



deck = build_deck()
player_one = build_hand(deck)
player_two = build_hand(deck)


#print(player_one)
#print(player_two)
#print(len(deck))

print(play_game(player_one, player_two))