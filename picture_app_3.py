import unittest
from unittest.mock import patch

# Globals
MIN_SIZE = 3
MAX_SIZE = 15


# Methods
def get_square():
    min_size = 1
    max_size = MAX_SIZE
    num = get_size(min_size, max_size)
    square = ''
    for i in range(num):
        square += '*****\n'
    return square


def get_size(min_size, max_size):
    is_valid_input = False
    while not is_valid_input:
        try:
            size = int(input(f'Please enter a size between {min_size} and {max_size}: '))
            if max_size >= size >= min_size:
                return size
            else:
                print(f'You entered \"{size}\". Please enter a number between {min_size} and {max_size}')
        except ValueError:
            print(f'Please enter a number between {min_size} and {max_size}')


def get_box():
    num = get_size(MIN_SIZE, MAX_SIZE)
    box = ''
    for i in range(num + 1):
        if i == 0 or i == num:
            box += '*****\n'
        else:
            box += '*   *\n'
    return box


def get_diagonal_down():
    size = get_size(MIN_SIZE, MAX_SIZE)
    row = ''
    for i in range(size):
        row += ' ' * i + '*\n'
    return row


def get_diagonal_up():
    size = get_size(MIN_SIZE, MAX_SIZE)
    row = ''
    for i in range(size):
        row += ' ' * (size - i - 1) + '*\n'
    return row


def get_checker_board():
    min_size = 5
    size = get_size(min_size, MAX_SIZE)
    checker_board = ''
    for i in range(size):
        if i % 2 == 0:
            checker_board += '* * * * * * *\n'
        else:
            checker_board += ' * * * * * * \n'
    return checker_board


def get_help():
    return "acceptable commands: help, quit, square, box, diagonaldown, diagonalup, checkerboard"


# Main
def main():
    user_prompts = {
        'help': get_help,
        'square': get_square,
        'box': get_box,
        'diagonaldown': get_diagonal_down,
        'diagonalup': get_diagonal_up,
        'checkerboard': get_checker_board
    }

    not_quit = False
    while not not_quit:
        command = input(f"Please enter a command\n({get_help()}): \n").lower().strip()

        if command not in user_prompts:
            print("Please enter a valid command.")
        else:
            print(user_prompts[command]())

        if command == 'quit':
            print('Goodbye')
            break


if __name__ == '__main__':
    main()


class TestShapesApp(unittest.TestCase):

    @patch('builtins.input', side_effect=['5'])
    def test_get_square(self, mock_input):
        expected_output = '*****\n*****\n*****\n*****\n*****\n'
        self.assertEqual(get_square(), expected_output)

    @patch('builtins.input', side_effect=['5'])
    def test_get_box(self, mock_input):
        expected_output = '*****\n*   *\n*   *\n*   *\n*   *\n*****\n'
        self.assertEqual(get_box(), expected_output)

    @patch('builtins.input', side_effect=['5'])
    def test_get_diagonal_down(self, mock_input):
        expected_output = '*\n *\n  *\n   *\n    *\n'
        self.assertEqual(get_diagonal_down(), expected_output)

    @patch('builtins.input', side_effect=['5'])
    def test_get_diagonal_up(self, mock_input):
        expected_output = '    *\n   *\n  *\n *\n*\n'
        self.assertEqual(get_diagonal_up(), expected_output)

    @patch('builtins.input', side_effect=['7'])
    def test_get_checker_board(self, mock_input):
        expected_output = '* * * * * * *\n * * * * * * \n* * * * * * *\n * * * * * * \n* * * * * * *\n * * * * * * \n* * * * * * *\n'
        self.assertEqual(get_checker_board(), expected_output)

    def test_get_help(self):
        expected_output = "acceptable commands: help, quit, square, box, diagonaldown, diagonalup, checkerboard"
        self.assertEqual(get_help(), expected_output)

    @patch('builtins.input', side_effect=['20', '5'])
    def test_get_size_out_of_bounds_high(self, mock_input):
        with self.assertRaises(ValueError):
            get_size(MIN_SIZE, MAX_SIZE)

    @patch('builtins.input', side_effect=['1', '2', '3'])
    def test_get_size_out_of_bounds_low(self, mock_input):
        result = get_size(MIN_SIZE, MAX_SIZE)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
