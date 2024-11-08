import unittest


def minmax(lst: list[int]) -> tuple[int, int]:
    min_num = lst[0]
    mid = len(lst) // 2
    max_num = 0

    for i in range(len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]
        elif lst[i] > max_num:
            max_num = lst[i]

    return min_num, max_num


def test_minmax():
    if minmax([1, 2, 3]) != (1, 3):
        print("Error with minmax([1, 2, 3])")
    elif minmax([1, 3, 2, 4, 5, 6]) != (1, 6):
        print("Error with minmax([1, 2, 3, 4, 5, 6])")
    else:
        print("minmax([1, 2, 3]) passed")


if __name__ == "__main__":
    test_minmax()


def all_pairs(x, y):
    lst = []
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[i] != y[j]:
                lst += [x[i], y[j]]

    return lst


def list_to_dict(lst):
    dict = {}
    for i in range(len(lst)):
        dict[i + 1] = lst[i]

    return dict


def invert_dict(dict):
    temp = {}
    for val, key in dict.items():
        temp[key] = val
    return temp


def adds_to_target(list, target):
    set_list = set(list)
    for i in range(len(list)):
        for j in range(len(list)):
            if set_list(i) + set_list.pop(j) == target:
                return True
    return False


class MyTestCase(unittest.TestCase):
    def test_minmax(self):
        self.assertEqual(minmax([]), ())

        self.assertEqual(minmax([1, 2, 3]), (1, 3))
        self.assertEqual(minmax([6, 5, 4, 3, 2, 1]), (1, 6))
        self.assertEqual(minmax([6, 3, 4, 5, 2, 1]), (1, 6))

    def test_all_pairs(self):
        x = [1, 4, 6, 8]
        y = [5, 2, 6]
        expected = [1, 5, 1, 2, 1, 6, 4, 5, 4, 2, 4, 6, 6, 5, 6, 2, 8, 5, 8, 2, 8, 6]

        self.assertEqual(all_pairs(x, y), expected)

    def test_list_to_dict(self):
        lst = [2, 6, 6, 1, 7, 9]
        self.assertEqual(list_to_dict(lst), {1: 2, 2: 6, 3: 6, 4: 1, 5: 7, 6: 9})

    def test_invert_dict(self):
        self.assertEqual(invert_dict({1: 2, 2: 3, 3: 4}), {2: 1, 3: 2, 4: 3})

    def test_adds_to_target(self):
        self.assertEqual(adds_to_target([1, 6, 7, 3, 7, 10, 3], 13), True)
