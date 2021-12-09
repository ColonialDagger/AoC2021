import struct


def part1(data):
    occurences = 0

    for line in data:
        for signal in line[1]:
            if signal.__len__() in [2, 3, 4, 7]:
                occurences += 1

    return occurences


def part2(data):
    for line in data:
        key = [[] for x in range(10)]

        while not all(key):
            for decode in line[0]:
                letters = ''.join(sorted(decode))

                if letters.__len__() == 2:
                    if decode not in key[1]: key[1].append(decode)
                elif letters.__len__() == 3:
                    if decode not in key[7]: key[7].append(decode)
                elif letters.__len__() == 4:
                    if decode not in key[4]: key[4].append(decode)
                elif letters.__len__() == 5:
                    if decode not in key[2]: key[2].append(decode)
                    if decode not in key[3]: key[3].append(decode)
                    if decode not in key[5]: key[5].append(decode)
                elif letters.__len__() == 6:
                    if decode not in key[0]: key[0].append(decode)
                    if decode not in key[6]: key[6].append(decode)
                    if decode not in key[9]: key[9].append(decode)
                elif letters.__len__() == 7:
                    if decode not in key[8]: key[8].append(decode)

            print()

        print()


if __name__ == '__main__':
    testing = True

    print('Analyzing display signals...')
    file = 'testinput.txt' if testing else 'input.txt'

    with open(file) as f:
        input_ = f.readlines()
        f.close()

        # Line Processing
        data = []
        for line in input_:
            sig = []
            for sub in line.split(' | '):
                sig.append(sub.strip().split(' '))
            data.append(sig)

        # Cleanup
        del input_
        del line
        del sig
        del sub
        del file
        del f

    print(f'By analyzing outputs, it can be determined that the digits 1, 4, 7, and 8 appear {part1(data)} times.')
    print(f'The sum of all output values is {part2(data)}')
