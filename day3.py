import time
import re

INPUT_FILE = './inputs/3.input'

def tallyMuls(line):
    total = 0
    matches = re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)", line)
    for match in matches:
        a, b, = re.findall(r"[\d]{1,3}", match)
        total += int(a) * int(b)
    return total

def part1():
    with open(INPUT_FILE) as f:
        lines = f.read().split('\n')
        total = sum([tallyMuls(line) for line in lines])
        print(f'Part 1: {total}')
    
def part2():
    with open(INPUT_FILE) as f:
        line = f.read()

        total = 0
        for goodSeg in line.split("do()"):
            goodSeg = goodSeg.split("don't()")[0]
            total += tallyMuls(goodSeg)
            
        print(f'Part 2: {total}')

def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)

print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')