def is_prime(number):
    if number <= 1:
        return False
    if number <= 2 or number % 2 == 1:
        return True
    return False


def is_anagram(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    if word_one == word_two:
        return True

    for letter in word_one:
        if letter not in word_two:
            return False

    return True


def is_palindrome(word_one, word_two):
    if word_one == word_two[::-1]:
        return True
    return False


def is_anagram_set(anagram_list):
    for i in range(len(anagram_list) - 1):
        if is_anagram(anagram_list[i], anagram_list[i + 1]):
            print(anagram_list[i], anagram_list[i + 1])
        else:
            print("False:", anagram_list[i], anagram_list[i + 1])
            return False

    return True


def test_is_anagram():
    assert is_anagram("hello", "hello") == True
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "bello") == False
    assert is_anagram("hello", "helloo") == False
    assert is_anagram_set(["listen", "silent", "enlist"]) == True
    assert is_anagram_set(["hello", "world", "python"]) == False
    assert is_anagram_set(["Debit card", "Bad credit", "Bad credit"]) == True
    assert is_anagram_set(["Astronomer", "Moon starer", "No more stars"]) == False
    assert is_anagram_set([]) == True


def test_is_anagram_set():
    assert is_anagram_set(strs_2) == True
    assert is_anagram_set(strs) == False


def test_is_palindrome():
    assert is_palindrome("hello") == True


def generate_primes(n_max):
    """
    Generate a list of prime numbers up to n_max using the sieve of Eratosthenes.

    Parameters:
    n_max (int): The maximum number up to which to generate primes.

    Returns:
    list: A list of prime numbers up to n_max.

    Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    sieve = [True] * (n_max + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not primes
    for i in range(2, int(n_max**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n_max + 1, i):
                sieve[j] = False  # Mark multiples of i as non-prime
    primes = [i for i, prime in enumerate(sieve) if prime]

    return primes


def test_is_prime():
    prime = generate_primes(7500)
    prime_set = set(prime)
    prime_sm_list = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(9) == False
    assert is_prime(97) == True
    assert is_prime(7500) == False

    for n in prime_sm_list:
        assert is_prime(n) == True
    for n in prime:
        assert is_prime(n) == (n in prime_set)


def zigzag(s, k):
    """
    Arrange a string into a zigzag pattern across k lines.

    Parameters:
    s (str): The input string to be converted into zigzag pattern.
    k (int): The number of lines to span the zigzag pattern.

    Returns:
    str: A string representing the zigzag pattern.

    Example:
    >>> print(zigzag("ZigZagString", 3))
    Z   a   r
     i Z g t i g
      g   S   n
    """
    if k == 1 or k >= len(s):
        return s  # No zigzag needed

    # Initialize variables
    rows = [""] * k
    row = 0  # Current row
    step = 1  # Direction of traversal
    pos = 0  # Current position in the original string

    # List to keep track of the current length of each row
    row_lengths = [0] * k

    for char in s:
        # Calculate spaces needed before the character
        spaces_needed = pos - row_lengths[row]
        rows[row] += " " * spaces_needed + char
        row_lengths[row] = pos + 1  # Update the length of the current row

        # Move to the next row
        if row == 0:
            step = 1
        elif row == k - 1:
            step = -1
        row += step
        pos += 1

    # Join the rows with newline characters
    result = "\n".join(row.rstrip() for row in rows)
    return result


def test_zigzag():
    """
    Test cases for the zigzag function.
    """
    # Test Case 1: Basic functionality with k=3
    input_string = "ZigZagString"
    k = 3
    expected_output = "Z   a   r\n i Z g t i g\n  g   S   n"
    assert zigzag(input_string, k) == expected_output, "Test Case 1 Failed"

    # Test Case 2: Edge case with k=1 (should return the original string)
    input_string = "HelloWorld"
    k = 1
    expected_output = "HelloWorld"
    assert zigzag(input_string, k) == expected_output, "Test Case 2 Failed"

    # Test Case 3: Edge case with k greater than length of string (should return original string)
    input_string = "Hi"
    k = 5
    expected_output = "Hi"
    assert zigzag(input_string, k) == expected_output, "Test Case 3 Failed"

    # Test Case 4: Empty string input
    input_string = ""
    k = 3
    expected_output = ""
    assert zigzag(input_string, k) == expected_output, "Test Case 5 Failed"


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs_2 = ["eat", "tea", "tea", "ate", "tea", "eat"]
    input_string = "ZigZagString"
    k = 3

    test_is_anagram_set()
    test_is_prime()
    test_is_anagram()
    print(is_palindrome("eat", "tae"))
    print(is_palindrome("bat", "tab"))
    print(zigzag(input_string, k))
    print(zigzag("HelloWorld", 5))

    test_zigzag()
