if __name__ == '__main__':

    # Reads lines into a list of int-type members
    with open('input.txt') as f:
        depths = list(map(int, f.readlines()))

    # Part 1
    print('\nPart 1 Analysis...')
    oldDepth = False
    incDepth = 0
    decDepth = 0
    noChangeDepth = 0
    for i in depths:
        newDepth = i
        if not oldDepth:
            print(str(newDepth) + ' (N/A - no previous measurement)')
        elif oldDepth == newDepth:
            print(str(newDepth) + ' (no change)')
            noChangeDepth += 1
        elif oldDepth < newDepth:
            print(str(newDepth) + ' (increased)')
            incDepth += 1
        elif oldDepth > newDepth:
            print(str(newDepth) + ' (decreased)')
            decDepth += 1
        oldDepth = newDepth

    # Part 2
    print('\nPart 1 Analysis...')
    oldSum = False
    incSum = 0
    decSum = 0
    noChangeSum = 0
    for i in range(depths.__len__()-2):
        newSum = depths[i] + depths[i+1] + depths[i+2]
        if not oldSum:
            print(str(newSum) + ' (N/A - no previous measurement)')
        elif oldSum == newSum:
            print(str(newSum) + ' (no change)')
            noChangeSum += 1
        elif oldSum < newSum:
            print(str(newSum) + ' (increased)')
            incSum += 1
        elif oldSum > newSum:
            print(str(newSum) + ' (decreased)')
            decSum += 1
        oldSum = newSum

    print('\n-----------Part 1 Statistics-----------')
    print('Initial Depth: ' + str(depths[0]))
    print('Final Depth: ' + str(depths[-2]))
    print('Δ Depth: ' + str(int(depths[-1])-int(depths[0])))
    print('Number of times increased: ' + str(incDepth))
    print('Number of times decreased: ' + str(decDepth))
    print('Number of times with no depth change: ' + str(noChangeDepth))
    print('-----------Part 2 Statistics-----------')
    print('Number of times increased: ' + str(incSum))
    print('Number of times decreased: ' + str(decSum))
    print('Number of times with no depth change: ' + str(noChangeSum))
    print('---------------------------------------')
