def occurence_counter(input, i):
    zeroes = 0
    ones = 0

    for n in input:

        if n[i] == '0':
            zeroes += 1
        elif n[i] == '1':
            ones += 1

    return zeroes, ones


if __name__ == '__main__':

    # Reads lines into a list of int-type members
    print('Reading diagnostic report...')
    with open('input.txt') as f:
        input = list(map(str, f.readlines()))
        n = 0
        for i in input:
            input[n] = i.strip()
            n += 1

    # Part 1
    print('Processing...')
    gamma_rate = []
    hex_rate = []

    for i in range(input[0].__len__()):

        zeroes, ones = occurence_counter(input, i)
        if zeroes > ones:
            gamma_rate.append('0')
            hex_rate.append('1')
        elif zeroes < ones:
            gamma_rate.append('1')
            hex_rate.append('0')

    gamma_rate = int(''.join(gamma_rate), 2)
    hex_rate = int(''.join(hex_rate), 2)

    print(f'Gamma rate: {gamma_rate}')
    print(f'Hex rate: {hex_rate}')
    print(f'Submarine power consumption: {gamma_rate*hex_rate} GW\n')

    # Part 2
    print('Verifying life support...')

    # Oxygen generator rating finder
    oxygen_rating = input
    for i in range(oxygen_rating[0].__len__()):  # i = character in string
        zeroes, ones = occurence_counter(oxygen_rating, i)  # Occurrence counter

        if zeroes > ones:  # Filter
            keep = [n for n in oxygen_rating if n[i] == '0']
        elif zeroes <= ones:
            keep = [n for n in oxygen_rating if n[i] == '1']
        oxygen_rating = keep

        if oxygen_rating.__len__() == 1:  # Exits early if one item remains
            break

    oxygen_rating = int(oxygen_rating[0], 2)

    # CO2 rating finder
    co2_rating = input
    for i in range(co2_rating[0].__len__()):  # i = character in string
        zeroes, ones = occurence_counter(co2_rating, i)  # Occurrence counter

        if zeroes <= ones:  # Filter
            keep = [n for n in co2_rating if n[i] == '0']
        elif zeroes > ones:
            keep = [n for n in co2_rating if n[i] == '1']
        co2_rating = keep

        if co2_rating.__len__() == 1:  # Exits early if one item remains
            break

    co2_rating = int(co2_rating[0], 2)

    print(f'Oxygen rating: {oxygen_rating}')
    print(f'CO2 scrubber rating: {co2_rating}')
    print(f'Life support rating: {oxygen_rating*co2_rating}')

