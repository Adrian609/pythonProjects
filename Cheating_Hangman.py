import random
import unittest
from collections import defaultdict
from itertools import cycle
from unittest.mock import patch


def mask_word(word, guessed):
    """Mask the word by replacing unguessed letters with hyphens."""
    return "".join(letter if letter in guessed else "-" for letter in word)


def partition(words, guessed):
    """Partition the set of words based on the guessed letters."""
    partitions = defaultdict(set)
    for word in words:
        hint = mask_word(word, guessed)
        partitions[hint].add(word)
    return partitions


def max_partition(partitions):
    """Find the hint for the largest partite set."""
    max_size = 0
    candidates = []

    for hint, words in partitions.items():
        size = len(words)
        revealed_count = sum(1 for c in hint if c != "-")
        if size > max_size:
            max_size = size
            candidates = [(hint, revealed_count)]
        elif size == max_size:
            candidates.append((hint, revealed_count))

    # Sort by fewest revealed letters; break ties randomly
    return (
        sorted(candidates, key=lambda x: (x[1], random.random()))[0][0]
        if candidates
        else None
    )


def play_hangman(words, word_length, show_details=False):
    """Play the cheating Hangman game."""
    filtered_words = {word for word in words if len(word) == word_length}
    if not filtered_words:
        print(f"No words of length {word_length} found.")
        return

    guessed = set()
    remaining_guesses = 5
    current_hint = "-" * word_length

    while remaining_guesses > 0:
        if "-" not in current_hint:
            print(f"You win! The word was {current_hint}.")
            return

        print(f"You have {remaining_guesses} guesses remaining")
        print(f"Guessed letters: {guessed}")
        print(f"Current hint: {current_hint}")

        guess = input("Enter a letter: ").lower()
        if guess in guessed:
            print("That letter has already been guessed.")
            continue

        guessed.add(guess)
        partitions = partition(filtered_words, guessed)

        if show_details:
            print("Partitions:")
            for hint, words in partitions.items():
                print(f"{hint}: {words}")

        next_hint = max_partition(partitions)
        filtered_words = partitions[next_hint]

        if current_hint == next_hint:
            remaining_guesses -= 1
            print(f"I'm sorry, '{guess}' is not in the word.")
        else:
            print(f"Yes! '{guess}' is in the word!")

        current_hint = next_hint

    print(f"You have lost. The word was {random.choice(list(filtered_words))}.")


def main():
    """Run the Hangman game."""
    file_path = "dictionary.txt"
    try:
        with open(file_path) as f:
            words = [line.strip() for line in f if line.strip()]

        word_length = int(input("What word length? "))
        show_details = word_length < 0
        play_hangman(words, abs(word_length), show_details)
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except FileNotFoundError:
        print(f"Dictionary file not found at: {file_path}")


class TestHangman(unittest.TestCase):
    def test_mask_word(self):
        self.assertEqual(mask_word("zymurgy", {"r", "s", "t", "n", "e"}), "----r--")
        self.assertEqual(mask_word("zymurgy", {"y", "m"}), "-ym---y")
        self.assertEqual(mask_word("apple", set()), "-----")
        self.assertEqual(mask_word("banana", {"a"}), "-a-a-a")

    def test_partition(self):
        words = {"abcd", "abce", "abdg"}
        guessed = {"a", "b"}
        partitions = partition(words, guessed)
        self.assertEqual(partitions, {"ab--": {"abcd", "abce", "abdg"}})

        guessed = {"a", "b", "c"}
        partitions = partition(words, guessed)
        self.assertEqual(partitions, {"abc-": {"abcd", "abce"}, "ab--": {"abdg"}})

    def test_max_partition(self):
        partitions = {"abc-": {"abcd", "abce"}, "ab--": {"abdg", "abdf"}}
        self.assertEqual(max_partition(partitions), "ab--")

        partitions = {"abcd": {"abcd"}, "abce": {"abce"}}
        self.assertIn(max_partition(partitions), ["abcd", "abce"])

    @patch("builtins.input", side_effect=cycle(["e", "a", "i", "o", "u", "t", "r"]))
    @patch("builtins.print")
    def test_play_hangman(self, mock_print, mock_input):
        words = ["wave", "quiz", "shiv", "wavy", "jinx", "onyx", "waxy"]
        play_hangman(words, 4, show_details=False)
        output = [call[0][0] for call in mock_print.call_args_list]
        self.assertIn("You have 5 guesses remaining", output[0])
        self.assertIn("You have lost", output[-1])

    @patch("builtins.input", side_effect=["x", "w", "a", "v", "y"])
    @patch("builtins.print")
    def test_play_hangman_win(self, mock_print, mock_input):
        words = ["wavy"]
        play_hangman(words, 4, show_details=False)
        output = [call[0][0] for call in mock_print.call_args_list]
        self.assertIn("You win! The word was wavy.", output)


user_input = int(input("Select:\n 1 - to run the program\n 2 - to run the test\n"))

if user_input == 1:
    print("Cheating Hangman!")
    main()
else:
    TestHangman()
