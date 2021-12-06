import numpy as np
import collections


def fastTick(fish, days):
    """Calculates the number of fish"""
    count = collections.Counter({
        -1: 0,
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    })
    for n in fish:  # Processes fish into counter
        count[n] += 1

    for day in range(1, days+1):
        print(f'Simulating day {day}...')

        for i in range(-1, 8):  # Ticks counter by shifting all values down by one index
            count[i] = count.get(i+1)
        count[8] = 0  # There will always be zero 8 tick fish after shifting but before births

        new_fish = count.get(-1)
        count[6] += new_fish
        count[8] += new_fish

        count[-1] = 0  # Resets -1 counter after births are complete

    return count


def tickDay(fish):
    """This is the original tick method that was used. While functional, this method is extremely slow."""
    fish -= 1  # Ticks day

    # Adds however many new fish are needed based on the -1's present
    for i in range((fish == -1).sum()):
        fish = np.append(fish, 8)

    fish = np.where(fish == -1, 6, fish)  # Resets fish counters upon expiring
    return fish


if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Counting lanternfish...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        input = np.array(list(map(int, f.read().split(','))))

    # This is a counter method of calculating fish count.
    days = 256
    print(f'''Initial State: {','.join(list(map(str, fish.tolist())))}''')
    print(f'\nThere are {sum(fastTick(input, days).values())} lanternfish surrounding the submarine. Recommend deploying fish repellent.')

