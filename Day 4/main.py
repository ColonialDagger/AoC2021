from typing import List

def bingo_win_check(board):

    # Check rows
    for row in board:
        if not any(row):
            return True

    for col in range(board.__len__()):
        check = []
        for row in board:
            check.append(row[col])
        if not any(check):
            return True

    return False


if __name__ == '__main__':

    # Reads lines into a list of int-type members
    print('Reading bingo data...')
    with open('input.txt') as f:
        input = list(map(str, f.readlines()))
        numbers = list(map(int, input.pop(0).strip().split(',')))

        # Process boards into 3D int array
        boards: list[list[list[int]]] = []
        current_board = []
        current_line = []
        input.pop(0)
        for line in input:
            if line != '\n':
                line = line.strip().split(' ')
                while '' in line:  # Filters out double spaces
                    line.remove('')
                for i in line:
                    current_line.append(int(i))
                current_board.append(current_line)
                current_line = []
            else:
                boards.append(current_board)
                current_board = []

        input = boards  # Re-initializes input for later use

    # Play Bingo!
    first = True
    for number in numbers:

        # Evaluate every board, replace with True if marked
        for idb, board in enumerate(boards):
            for idr, row in enumerate(board):
                for idc, col in enumerate(row):
                    if col == number:
                        boards[idb][idr][idc] = False  # Because ints return true, marks false for checking later

        # Check for a winner
        for idb, board in enumerate(boards):
            if bingo_win_check(board):
                if first:  # Gets first winner for part 1
                    winner = board
                    first = False
                last_winner = [board, number]  # Gets last winner for part 2
                boards.pop(idb)

    # Gets solution for part 1
    solution = 0
    for i in winner:
        for n in i:
            if n:
                solution += n
    solution *= number
    print(f'Part 1 score: {solution}')

    # Gets solution for part 2
    solution = 0
    for i in last_winner[0]:
        for n in i:
            if n:
                solution += n
    solution *= last_winner[1]
    print(f'Part 2 score: {solution}')