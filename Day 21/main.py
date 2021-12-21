
class Player:
    def __init__(self, position):
        self.score = 0
        self.position = position


class Dice:
    def __init__(self, max_roll):
        self.current = 0
        self.max_roll = max_roll

    def roll(self):
        # self.current = self.current + 1 if self.current <= self.max_roll else self.current = self.current - 99
        self.current += 1
        if self.current > self.max_roll:
            self.current -= self.max_roll
        return self.current


def part1(data):
    dice = Dice(100)
    turn = 0
    players = []

    for n in data:
        players.append(Player(n))

    while players[0].score < 1000 and players[1].score < 1000:
        for n in range(3):
            players[turn % 2].position += dice.roll()

        # current = players[turn % 2].position % 10 if players[turn % 2].position % 10 != 0 else 10
        if players[turn % 2].position % 10 != 0:
            players[turn % 2].score += players[turn % 2].position % 10
        else:
            players[turn % 2].score += 10

        turn += 1

    winner = players[(turn-1) % 2]
    loser = players[turn % 2]
    return loser.score * turn*3


if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Loading player positions...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        data = f.readlines()
        for i, line in enumerate(data):
            data[i] = int(line[-2])

    print(f'The losing value is {part1(data)}.')
