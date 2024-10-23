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
    if not hand1 or not hand2:
        return 0  # If any player has no cards, no hand is played.

    common_pool = [hand1.pop(0), hand2.pop(0)]
    winner = check_winner(common_pool[0], common_pool[1])

    if winner == 1:
        random.shuffle(common_pool)
        hand1.extend(common_pool)
    elif winner == 2:
        random.shuffle(common_pool)
        hand2.extend(common_pool)
    else:
        # Handle the war scenario (tie)
        winner = draw(hand1, hand2, common_pool)
        if winner == 1:
            random.shuffle(common_pool)
            hand1.extend(common_pool)
        elif winner == 2:
            random.shuffle(common_pool)
            hand2.extend(common_pool)


def play_hands(player_one, player_two):
    """Simulates the game until one player wins or the game draws."""
    hand_count = 0
    while player_one and player_two:
        play_hand(player_one, player_two)
        hand_count += 1

    if not player_one and not player_two:
        return hand_count, "draw"
    elif not player_one:
        return hand_count, "player one lost"
    elif not player_two:
        return hand_count, "player two lost"


def simulate_games(num_simulations):
    """Simulates multiple games and calculates the average number of hands."""
    total_hands = 0
    player_one_wins = 0
    player_two_wins = 0
    draws = 0

    for _ in range(num_simulations):
        deck = build_deck()
        player_one, player_two = build_hand(deck)
        hand_count, result = play_hands(player_one, player_two)
        total_hands += hand_count

        if result == "player one lost":
            player_two_wins += 1
        elif result == "player two lost":
            player_one_wins += 1
        else:
            draws += 1

    average_hands = total_hands / num_simulations
    print(f"Average number of hands per game: {average_hands}")
    print(f"Player 1 wins: {player_one_wins}")
    print(f"Player 2 wins: {player_two_wins}")
    print(f"Draws: {draws}")


def draw(hand1, hand2, common_pool):
    """Handles the draw scenario, adding more cards to the common pool until a winner is determined."""
    while True:
        if len(hand1) < 2:
            return 2  # Player 1 loses as they can't continue the war
        elif len(hand2) < 2:
            return 1  # Player 2 loses as they can't continue the war

        # Each player adds one card face-down and one card face-up
        common_pool.extend([hand1.pop(0), hand2.pop(0)])  # Face-down cards
        common_pool.extend([hand1.pop(0), hand2.pop(0)])  # Face-up cards

        # Check the face-up cards
        winner = check_winner(common_pool[-2], common_pool[-1])
        if winner != 0:
            return winner


def check_winner(card1, card2):
    """Determines the winner based on the card values."""
    if card1[0] > card2[0]:
        return 1
    elif card1[0] < card2[0]:
        return 2
    return 0  # Tie


# Test functions
def test_check_winner():
    """Tests check_winner function with predefined cases."""
    assert check_winner((14, "H"), (13, "S")) == 1, "Test failed: Player 1 should win"
    assert check_winner((13, "H"), (14, "S")) == 2, "Test failed: Player 2 should win"
    assert check_winner((10, "D"), (10, "C")) == 0, "Test failed: Should be a tie"
    print("All tests passed for check_winner function.")


def test_build_deck():
    """Tests the build_deck function."""
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


def test_play_hand():
    """Tests the play_hand function."""
    player1 = [(14, "H")]  # Ace of Hearts
    player2 = [(13, "S")]  # King of Spades
    play_hand(player1, player2)
    assert len(player1) == 2, "Test failed: Player 1 should have 2 cards"
    assert len(player2) == 0, "Test failed: Player 2 should have 0 cards"
    print("All tests passed for play_hand function.")


# Run test cases
test_check_winner()
test_build_deck()
test_play_hand()


# Simulate games
num_simulations = int(input("How many simulations would you like to play? "))
simulate_games(num_simulations)
