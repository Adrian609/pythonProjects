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
                print('Please enter a number between 3 and 15')
        except ValueError:
            print("Please enter a valid integer.")


def get_box():
    num = get_size(MIN_SIZE, MAX_SIZE)
    box = ''
    for i in range(num + 1):
        if 1 < i < num:
            box += '*   *\n'
        elif i == num or 0 == i:
            box += '*****\n'
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
