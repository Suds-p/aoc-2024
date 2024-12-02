from collections import Counter
with open('input') as f:
    lines = f.read().split('\n')

    left, right = [], []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    lcount = Counter(left)
    rcount = Counter(right)
    commonElems = set(left).intersection(right)

    totalDist = sum([abs(left[i] - right[i]) for i in range(len(left))])
    print(f'Day 1: {totalDist}')

    diffSum = 0 

    for elem in commonElems: 
        diffSum += elem * lcount[elem] * rcount[elem]

    print(f'Day 2: {diffSum}')
    
    