if __name__ == '__main__':

    # Reads lines into a list of int-type members
    with open('input.txt') as f:
        input = f.readlines()
        n = 0
        for i in input:  # Splits input
            input[n] = i.split(' ')
            input[n][1] = int(input[n][1])
            n += 1

    # Part 1
    horizontal_position = 0
    depth = 0
    aim = 0
    for i in input:
        if i[0] == 'forward':
            horizontal_position += i[1]
        elif i[0] == 'down':
            depth += i[1]
        elif i[0] == 'up':
            depth -= i[1]
    print('Part 1 Answer: ' + str(horizontal_position*depth))

    # Part 1
    horizontal_position = 0
    depth = 0
    aim = 0
    for i in input:
        if i[0] == 'forward':
            horizontal_position += i[1]
            depth += aim * i[1]
        elif i[0] == 'down':
            aim += i[1]
        elif i[0] == 'up':
            aim -= i[1]
    print('Part 2 Answer: ' + str(horizontal_position*depth))
