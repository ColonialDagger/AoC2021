import numpy
import numpy as np

def part1(data, ticks=100):
    flashes = 0

    for tick in range(ticks):
        data += 1

        while np.any(data >= 10):
            for (y, x), value in np.ndenumerate(data):
                if value >= 10:
                    data[y][x] = -1
                    flashes += 1

                    # Propogate to neighbors
                    # [0] [1] [2]
                    # [3] [*] [4]
                    # [5] [6] [7]
                    if x > 0 and y > 0 and data[y-1][x-1] > -1: data[y-1][x-1] += 1
                    if y > 0 and data[y-1][x] > -1: data[y-1][x] += 1
                    if x < np.shape(data)[1]-1 and y > 0 and data[y-1][x+1] > -1: data[y-1][x+1] += 1
                    if x > 0 and data[y][x-1] > -1: data[y][x-1] += 1
                    if x < np.shape(data)[1]-1 and data[y][x+1] > -1: data[y][x+1] += 1
                    if x > 0 and y < np.shape(data)[0]-1 and data[y+1][x-1] > -1: data[y+1][x-1] += 1
                    if y < np.shape(data)[0]-1 and data[y+1][x] > -1: data[y+1][x] += 1
                    if x < np.shape(data)[1]-1 and y < np.shape(data)[0]-1 and data[y+1][x+1] > -1: data[y+1][x+1] += 1

        data = np.where(data == -1, 0, data)

    return flashes


def part2(data):
    tick = 0
    while not np.all(data == 0):
        data += 1
        tick += 1

        while np.any(data >= 10):
            for (y, x), value in np.ndenumerate(data):
                if value >= 10:
                    data[y][x] = -1

                    # Propogate to neighbors
                    # [0] [1] [2]
                    # [3] [*] [4]
                    # [5] [6] [7]
                    if x > 0 and y > 0 and data[y-1][x-1] > -1: data[y-1][x-1] += 1
                    if y > 0 and data[y-1][x] > -1: data[y-1][x] += 1
                    if x < np.shape(data)[1]-1 and y > 0 and data[y-1][x+1] > -1: data[y-1][x+1] += 1
                    if x > 0 and data[y][x-1] > -1: data[y][x-1] += 1
                    if x < np.shape(data)[1]-1 and data[y][x+1] > -1: data[y][x+1] += 1
                    if x > 0 and y < np.shape(data)[0]-1 and data[y+1][x-1] > -1: data[y+1][x-1] += 1
                    if y < np.shape(data)[0]-1 and data[y+1][x] > -1: data[y+1][x] += 1
                    if x < np.shape(data)[1]-1 and y < np.shape(data)[0]-1 and data[y+1][x+1] > -1: data[y+1][x+1] += 1

        data = np.where(data == -1, 0, data)

    return tick + 1


if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Analyzing dumbo octopus energy levels...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        data = f.readlines()
        for i, line in enumerate(data):
            data[i] = [int(char) for char in line.strip()]
        data = np.array(data, int)

    ticks = 100
    print(f'There will be {part1(data, ticks)} flashes in the next {ticks} ticks.')
    print(f'The octopuses flashes will synchronize at {part2(data)} ticks.')
