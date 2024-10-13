import random


def build_deck():
    suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
    values = list(range(2, 15))  # 2-10, J, Q, K, A (where A=14)
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck


def build_hand(card_deck):
    hand = []
    for i in range(0, 26):
        hand.append(card_deck.pop())
    return hand


def play_hand(hand1, hand2):
    common_pool = [hand1.pop(0), hand2.pop(0)]
    winner = check_winner(common_pool[0], common_pool[1])

    if winner == 1:
        random.shuffle(common_pool)  # Shuffle the pool to avoid infinite loops
        hand1.extend(common_pool)  # Add all cards in the pool to player 1
    elif winner == 2:
        random.shuffle(common_pool)
        hand2.extend(common_pool)

    return hand1, hand2


def play_hands(player_one, player_two):
    while len(player_one) != 0 and len(player_two) != 0:
        play_hand(player_one, player_two)
        if len(player_one) == 0:
            return "player one lost"
        if len(player_two) == 0:
            return "player two lost"


def check_winner(card1, card2):
    if card1 == card2:
        return 0
    elif card1 > card2:
        return 1
    elif card1 < card2:
        return 2

deck = build_deck()
player_one = build_hand(deck)
player_two = build_hand(deck)

print(play_hands(player_one, player_two))
print(f'player1: {len(player_one)}')
print(f'Player2: {len(player_two)}')


def test_check_winner():
    card1 = [(14, "H")]
    card2 = [(13, "H")]
    if check_winner(card1, card2) != 1:
        print(f"Error: expected player1 to win")
    else:
        print(f"test passed: player 1 wins")
