def get_square():
    num = get_size()
    square = ''
    for i in range(num):
        square += '*****\n'
    return square


def get_size():
    size = int(input('Please enter a size between 3 and 15: '))
    return size


def get_box():
    num = get_size()
    for i in range(num + 1):
        if 1 < i < num:
            print('*   *')
        elif i == num or 0 == i:
            print('*****')


def get_diagonal_down():
    size = get_size()
    row = ''
    for i in range(size):
        row += ' ' * i + '*\n'
    return row


def get_diagonal_up():
    size = get_size()
    row = ''
    for i in range(size):
        row += ' ' * (size - i - 1) + '*'
    return row


def get_checker_board():
    size = get_size()
    for i in range(size):
        if i % 2 == 0:
            print('* * * * *')
        else:
            print(' * * * * *')


def get_help():
    return "acceptable commands: help, quit, square, box, diagonaldown, diagonalup, checkerboard"


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
        command = input("Please enter a command: \n").lower().strip()

        if command not in {'help', 'quit', 'square', 'box', 'diagonaldown', 'diagonalup', 'checkerboard'}:
            print("Please enter a valid command.")
            print(get_help())
        else:
            print(user_prompts[command]())

        if command == 'quit':
            print('Goodbye')
            break


if __name__ == '__main__':
    main()
