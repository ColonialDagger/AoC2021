import numpy as np


def addLines(grid, i, straight=False):
    x1 = i[0][0]
    x2 = i[1][0]
    y1 = i[0][1]
    y2 = i[1][1]

    if straight:  # Returns without action if line given is diagonal but user prompts only for straight lines
        if x1 != x2 and y1 != y2:
            return

    grid[y1][x1] += 1  # Adds 1 to initial point
    while x1 != x2 or y1 != y2:

        # Navigate to next point needed
        if x2 > x1:
            x1 += 1
        elif x2 < x1:
            x1 -= 1

        if y2 > y1:
            y1 += 1
        elif y2 < y1:
            y1 -= 1

        grid[y1][x1] += 1


if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Reading hydrothermal data...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        input = []
        for i in f.readlines():
            coords = []
            for n in i.strip().split(' -> '):
                coords.append(list(map(int, n.split(','))))
            input.append(coords)

    # Creates array from input
    input = np.array(input)
    grid = np.zeros((input.max() + 1, input.max() + 1), np.int16)

    # Part 1 solution
    for i in input:
        addLines(grid, i, True)
    print(f'Warning: Hydrothermal temperatures are dangerously high at {(grid >= 2).sum()} points.',
          'It is strongly recommended that you turn back now.')

    # Part 2 solution
    grid = np.zeros((input.max() + 1, input.max() + 1), np.int16)
    for i in input:
        addLines(grid, i, False)
    print('Warning: Deeper analysis has reveal that hydrothermal temperatures are dangerously high at',
          f'{(grid >= 2).sum()} points. Are you sure whatever you are doing is worth it?')
