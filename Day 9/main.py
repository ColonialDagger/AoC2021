import numpy as np


def find_lows(data):
    lows = []
    risk = 0

    for y, row in enumerate(data):
        for x, col in enumerate(row):
            neighbor = [None, None, None, None]

            neighbor[0] = col < data[y-1][x] if y > 0 else None
            neighbor[1] = col < data[y+1][x] if y < data.__len__()-1 else None  # Evaluates down
            neighbor[2] = col < data[y][x-1] if x > 0 else None  # Evaluates left
            neighbor[3] = col < data[y][x+1] if x < len(row)-1 else None  # Evaluates right

            if all(list(filter(lambda i: i != None, neighbor))):
                lows.append([y, x, col])

    for n in lows:
        risk += n[2] + 1

    return lows, risk


def find_basins(data, lows):

    # Find edges
    edges = np.zeros((data.__len__(), data[0].__len__()), dtype=int)
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            edges[y][x] = col if col != 9 else -1

    # Find basins
    for row, col, low in lows:
        print()
    print()


if __name__ == '__main__':
    testing = True

    # Reads lines into a list input
    print('Reading heightmap data...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        fdata = f.readlines()
        data = []
        for line in fdata:
            line = line.strip()
            l = []
            for n in line:
                l.append(int(n))
            data.append(l)
        data = np.array(data)

        f.close()

    lows, risk = find_lows(data)

    print(f'There are {lows.__len__()} low points in the cave system, with a total risk level of {risk}.')
    print(f'Smoke will fill approximately {find_basins(data, lows)} basins.')



