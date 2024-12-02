from collections import Counter
import time

INPUT_FILE = './inputs/1.input'

def part1():
    with open(INPUT_FILE) as f:
        lines = f.read().split('\n')

        left, right = [], []
        for line in lines:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

        left.sort()
        right.sort()

        totalDist = sum([abs(left[i] - right[i]) for i in range(len(left))])
        print(f'Part 1: {totalDist}')
    
def part2():
    with open(INPUT_FILE) as f:
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

        diffSum = 0 

        for elem in commonElems: 
            diffSum += elem * lcount[elem] * rcount[elem]

        print(f'Part 2: {diffSum}')

def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)

print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')