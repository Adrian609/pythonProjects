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


def is_anagram_set(anagram_list):
    for i in range(len(anagram_list) - 1):
        if is_anagram(anagram_list[i], anagram_list[i + 1]):
            print(anagram_list[i], anagram_list[i + 1])
        else:
            print("False:", anagram_list[i], anagram_list[i + 1])
            return False

    return True


def test_is_anagram():
    assert is_anagram("hello", "helloo") == False
    assert is_anagram("hello", "hello") == True


def test_is_anagram_set():
    assert is_anagram_set(strs_2) == True
    assert is_anagram_set(strs) == False


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

    for n in prime_sm_list:
        assert is_prime(n) == True
    for n in prime:
        assert is_prime(n) == (n in prime_set)


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs_2 = ["eat", "tea", "tea", "ate", "tea", "eat"]

    test_is_anagram_set()
    test_is_prime()
    test_is_anagram()
