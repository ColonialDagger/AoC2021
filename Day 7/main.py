from collections import Counter
import statistics


def consume_part1(current: int, target: int) -> int:
    """Calculates part 1 fuel consumption using factorial addition.

    Args:
        current (int): current crab position
        target (int): target crab position

    Returns:
        int: fuel required to move crab"""
    return int(abs(current-target))


def consume_part2(current: int, target: int) -> int:
    """Calculates part 2 fuel consumption using factorial addition.

    Args:
        current (int): current crab position
        target (int): target crab position

    Returns:
        int: fuel required to move crab"""
    return sum(range(int(abs(current-target))+1))


def bruteforce(data: list, part1: bool) -> int:
    """This method will find the total consumption for moving to every single point between the 2 most outlying
    positions. This method is slow but it works in both Parts 1 and 2.

    Args:
        data (list): list of crab positions as integers
        part1 (bool): True if calculating for part 1, false for part 2

    Returns:
        int: (target, fuel_required) where target is target position and fuel_required is fuel needed to move all crabs
             to that position."""
    fuel_projections = Counter()

    for i in range(min(data), max(data)):
        fuel_consumed = 0
        for n in data:
            fuel_consumed += consume_part1(n, i) if part1 else consume_part2(n, i)
        fuel_projections[i] += fuel_consumed

    return fuel_projections.most_common()[-1]


def statistical_method(data: list, part1: bool) -> int:
    """This method will move all crabs to the statistical median.

    Args:
        data (list): list of crab positions as integers
        part1 (bool): True if calculating for part 1, false for part 2

    Returns:
        int: amount of fuel needed to move all crabs to the median position"""
    target = statistics.median(data) if part1 else statistics.mean(data).__floor__()
    fuel_consumed = 0
    for crab in data:
        fuel_consumed += consume_part1(crab, target) if part1 else consume_part2(crab, target)
    return fuel_consumed


if __name__ == '__main__':
    testing = True
    part1 = False

    # Reads lines into a list input
    print('Determining crab positions...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        data = list(map(int, f.read().split(',')))

    # target, fuel_required = bruteforce(data, part1)

    median_result = statistical_method(data, part1)

    print(f"{statistical_method(data, part1)} units of fuel are needed to align crabs.")
    print(f"After further analysis of factorial movement requirements, {statistical_method(data, part1)}"
          f" units of fuel are needed to align crabs.")
