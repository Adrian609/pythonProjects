import random


def build_deck():
    suits = ["H", "D", "C", "S"]  # Hearts, Diamonds, Clubs, Spades
    values = list(range(2, 15))  # 2-10, J, Q, K, A (where A=14)
    card_deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(card_deck)
    return card_deck


def build_hand(card_deck):
    hand1 = []
    hand2 = []
    for i in range(0, 26):
        hand1.append(card_deck.pop())
        hand2.append(card_deck.pop())
    return hand1, hand2


def play_hand(hand1, hand2):
    """Plays a single hand and adds cards to the winner's deck."""
    common_pool = [hand1.pop(0), hand2.pop(0)]
    winner = check_winner(common_pool[0], common_pool[1])

    if winner == 1:
        random.shuffle(common_pool)
        hand1.extend(common_pool)
    elif winner == 2:
        random.shuffle(common_pool)
        hand2.extend(common_pool)
    else:
        # Invoke draw() to handle the tie scenario
        winner = draw(hand1, hand2, common_pool)
        if winner == 1:
            random.shuffle(common_pool)
            hand1.extend(common_pool)
        elif winner == 2:
            random.shuffle(common_pool)
            hand2.extend(common_pool)


def play_hands(player_one, player_two):
    hand_count = 0
    while len(player_one) != 0 and len(player_two) != 0:
        play_hand(player_one, player_two)
        hand_count += 1
        if len(player_one) == 0:
            return hand_count, "player one lost"
        if len(player_two) == 0:
            return hand_count, "player two lost"


def simulate_games(num_simulations):
    total_hands = 0
    for _ in range(num_simulations):
        deck = build_deck()
        player_one, player_two = build_hand(deck)
        hand_count, _ = play_hands(player_one, player_two)
        total_hands += hand_count
    average_hands = total_hands / num_simulations
    print(f"Average number of hands per game: {average_hands}")


def draw(hand1, hand2, common_pool):
    """Handles the draw scenario, adding more cards to the common pool until a winner is determined."""
    while True:
        # Check if both players have enough cards for a war (minimum 2 cards)
        if len(hand1) < 2:
            return 2  # Player 1 loses as they can't continue the draw
        elif len(hand2) < 2:
            return 1  # Player 2 loses as they can't continue the draw

        # Add one card face-down and one card face-up from each player
        common_pool.extend([hand1.pop(0), hand2.pop(0)])  # Face-down cards
        common_pool.extend([hand1.pop(0), hand2.pop(0)])  # Face-up cards

        # Check the face-up cards and determine the winner
        face_up_card1 = common_pool[-2]
        face_up_card2 = common_pool[-1]
        winner = check_winner(face_up_card1, face_up_card2)

        if winner != 0:  # Break the loop if there is a winner
            return winner


def check_winner(card1, card2):
    if card1[0] > card2[0]:
        return 1
    elif card1[0] < card2[0]:
        return 2
    return 0  # tie


deck = build_deck()
player_one, player_two = build_hand(deck)

# print(play_hands(player_one, player_two))
# print(f"player1: {len(player_one)}")
# print(f"Player2: {len(player_two)}")

num_simulations = int(input("How many simulations would you like to play? "))
simulate_games(num_simulations)


# Test functions
def test_check_winner():
    """Tests check_winner function with predefined cases."""
    assert check_winner((14, "H"), (13, "S")) == 1, "Test failed: Player 1 should win"
    assert check_winner((13, "H"), (14, "S")) == 2, "Test failed: Player 2 should win"
    assert check_winner((10, "D"), (10, "C")) == 0, "Test failed: Should be a tie"
    print("All tests passed for check_winner function.")


def test_build_deck():
    deck = build_deck()
    assert len(deck) == 52
    unique_cards = set(deck)
    assert len(unique_cards) == 52, "Test failed: Deck contains duplicate cards."
    expected_values = set(range(2, 15))  # 2 through 14 (Aces are 14)
    expected_suits = {"H", "D", "C", "S"}
    deck_values = {card[0] for card in deck}
    deck_suits = {card[1] for card in deck}
    assert deck_values == expected_values, "Test failed: Deck has incorrect values."
    assert deck_suits == expected_suits, "Test failed: Deck has incorrect suits."
    print("All tests passed for build_deck function.")


# Run test cases
test_check_winner()
test_build_deck()
