import unittest


def minmax(lst: list[int]) -> tuple[int, int] | bool:
    if len(lst) != 0:
        min_num = lst[0]
        mid = len(lst) // 2
        max_num = 0

        for i in range(len(lst)):
            if lst[i] < min_num:
                min_num = lst[i]
            elif lst[i] > max_num:
                max_num = lst[i]
        return min_num, max_num
    return False


def all_pairs(x, y):
    lst = []
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[i] != y[j]:
                lst += [(x[i], y[j])]
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


def adds_to_target(lst, target):
    set_list = set(lst)
    check_val = 0
    for item in set_list:
        for second_item in set_list:
            if item != second_item:
                check_val = item + second_item
            if check_val == target:
                return True
    return False


if __name__ == "__main__":
    adds_to_target([1, 2, 3, 4, 5], 5)


class MyTestCase(unittest.TestCase):
    def test_minmax(self):
        self.assertEqual(minmax([]), False)
        self.assertEqual(minmax([1, 2, 3]), (1, 3))
        self.assertEqual(minmax([6, 5, 4, 3, 2, 1]), (1, 6))
        self.assertEqual(minmax([9, 3, 4, 5, 2, 1]), (1, 9))
        self.assertNotEqual(minmax([9, 3, 4, 5, 2, 1]), (1))

    def test_all_pairs(self):
        x = [1, 4, 6, 8]
        y = [5, 2, 6]
        expected = [
            (1, 5),
            (1, 2),
            (1, 6),
            (4, 5),
            (4, 2),
            (4, 6),
            (6, 5),
            (6, 2),
            (8, 5),
            (8, 2),
            (8, 6),
        ]
        result_2 = [
            (1, 2),
            (1, 5),
            (1, 6),
            (4, 2),
            (4, 5),
            (4, 6),
            (6, 2),
            (6, 5),
            (8, 2),
            (8, 5),
            (8, 6),
        ]
        self.assertEqual([], [], [])
        self.assertEqual(all_pairs(x, y), expected)
        self.assertEqual(all_pairs(sorted(x), y), expected)
        self.assertEqual(all_pairs(x, sorted(y)), result_2)
        self.assertNotEqual(all_pairs(x, y), [])

    def test_list_to_dict(self):
        lst = [2, 6, 6, 1, 7, 9]
        self.assertEqual([], [])
        self.assertEqual(list_to_dict(lst), {1: 2, 2: 6, 3: 6, 4: 1, 5: 7, 6: 9})
        self.assertEqual(
            list_to_dict([4, 5, 6, 7, 8, ""]), {1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: ""}
        )
        self.assertEqual(list_to_dict(["A", "B", "C"]), {1: "A", 2: "B", 3: "C"})
        self.assertEqual(
            list_to_dict(["A", "B", "C", 1, 2, 3]),
            {1: "A", 2: "B", 3: "C", 4: 1, 5: 2, 6: 3},
        )
        self.assertNotEqual(list_to_dict([4, 5, 6, 7, 8, ""]), {})

    def test_invert_dict(self):
        self.assertEqual(invert_dict({}), {})
        self.assertEqual(invert_dict({1: 2, 2: 3, 3: 4}), {2: 1, 3: 2, 4: 3})
        self.assertEqual(invert_dict({1: 2, 2: 0, 3: 0}), {2: 1, 0: 2, 0: 3})
        self.assertNotEqual(invert_dict({1: 2, 2: 3, 3: 4}), {1: 2, 2: 3, 3: 4})
        self.assertNotEqual(invert_dict({1: 2, 2: 3, 3: 4}), {})

    def test_adds_to_target(self):
        self.assertEqual(adds_to_target([], 14), False)
        self.assertEqual(adds_to_target([1, 6, 7, 3, 7, 10, 3], 13), True)
        self.assertEqual(adds_to_target([1, 6, 7, 3, 6, 8, 3], 14), True)
        self.assertEqual(adds_to_target([1, 2, 3, 4, 5, 8, 3], 14), False)
        self.assertEqual(adds_to_target([1], 14), False)
