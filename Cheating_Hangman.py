def mask_word(word, guessed):
    """Returns word with all letters not in guessed replaced with hyphens

    Args:
        word (str): the word to mask
        guessed (set): the guessed letters

    Returns:
        str: the masked word
    """
    masked_word = ""

    for letter in word:
        if letter in guessed:
            masked_word += letter
        else:
            masked_word += "-"

    return masked_word


def partition(words, guessed):
    """Generates the partitions of the set words based upon guessed

    Args:
        words (set): the word set
        guessed (set): the guessed letters

    Returns:
        dict: The partitions
    """


def max_partition(partitions):
    """Returns the hint for the largest partite set

    The maximum partite set is selected by selecting the partite set with
    1. The maximum size partite set
    2. If more than one maximum, prefer the hint with fewer revealed letters
    3. If there is still a tie, select randomly

    Args:
        partitions (dict): partitions from partition function

    Returns:
        str: hint for the largest partite set
    """


def test_mask_word():
    word_list = {"wave", "quiz", "shiv", "wavy", "jinx", "onyx", "waxy"}
    guessed = {"o", "n", "w", "z"}

    assert mask_word("onyx", guessed) == "on--", "Test Failed"


def test_partition():
    word_list = {"wave", "quiz", "shiv", "wavy", "jinx", "onyx", "waxy"}
    guessed = {"o", "n", "w", "z"}

    assert partition(word_list, guessed) == "on--", "Test Failed"


print(mask_word("onyx", {"o", "n", "w", "z"}))
test_mask_word()
test_partition()
