import time

INPUT_FILE = './inputs/2.input'

def isRowValid(row):
    isValid = True
    asc = row[1] - row[0]
    for i in range(1, len(row)):
        delta = row[i] - row[i-1]
        if not (delta * asc > 0 and 1 <= abs(delta) <= 3):
            isValid = False
            break
    return isValid

def part1():
    with open(INPUT_FILE) as f:
        lines = f.read().split('\n')
        validRows = 0

        for line in lines:
            row = [int(x) for x in line.split(' ')]
            validRows += 1 if isRowValid(row) else 0
        print(f'Part 1: {validRows}')

def part2():
    with open(INPUT_FILE) as f:
        lines = f.read().split('\n')
        validRows = 0

        for line in lines:
            row = [int(x) for x in line.split()]

            for i in range(len(row)):
                rowCopy = row.copy()
                rowCopy.pop(i)
                if isRowValid(rowCopy):
                    validRows += 1
                    break
            
        print(f'Part 2: {validRows}')


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)

print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')