from statistics import median


def convert(char):
    openings = ['(', '[', '{', '<']
    closings = [')', ']', '}', '>']
    if char in closings:
        char = '(' if char == ')' else chr(ord(char) - 2)
    elif char in openings:
        char = ')' if char == '(' else chr(ord(char) + 2)
    return char

def score_expected(char):
    score_book = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return score_book[char]


def score_missing(char):
    score_book = {')': 1, ']': 2, '}': 3, '>': 4}
    return score_book[char]


def get_score(data, part2):
    points = 0
    points_list = []
    data_copy = data.copy()
    for line in data:

        tmp = []
        openings = ['(', '[', '{', '<']
        closings = [')', ']', '}', '>']

        # Process string
        for char in line:

            # Look for unexpected characters
            if char in closings:
                char = convert(char)
                if tmp[-1] == char:
                    tmp = tmp[:-1]
                else:
                    char = convert(char)
                    points += score_expected(char)
                    tmp = tmp[:-1]
                    data_copy.remove(line)
                    break
            else:
                tmp.append(char)

        # Complete missing elements in line
        if part2:
            if tmp.__len__() > 0:
                missing_points = 0
                for char in reversed(tmp):
                    char = convert(char)
                    missing_points = missing_points * 5 + score_missing(char)
                points_list.append(missing_points)

    data = data_copy.copy()

    if part2:
        return median(points_list)
    else:
        return points, data


if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Scanning syntax...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        data = f.read().split('\n')

    score, data = get_score(data, False)
    print(f'The scanned set has a total syntax error score of {score}.')
    print(f'When accounting for missing closers, the total syntax error score rises to {get_score(data, True)}.')
