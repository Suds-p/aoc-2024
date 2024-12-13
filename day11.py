import time
INPUT = './inputs/11.input'

def part1():
    with open(INPUT) as f:
        BLINKS = 25
        allStones = [int(x) for x in f.read().split(" ")]
        
        def simulateBlink(stone):
            stones = []
            str_stone = str(stone)
            if stone == 0:
                return [1]
            elif len(str_stone) % 2 == 0:
                return [
                    int(str_stone[ : len(str_stone)//2]),
                    int(str_stone[len(str_stone)//2 : ]),
                ]
            else:
                return [stone * 2024]
        
        for i in range(BLINKS):
            newStones = []
            for stone in allStones:
                newStones.extend(simulateBlink(stone))
            allStones = newStones
        print(f'Part 1: {len(allStones)}')


def part2():
    with open(INPUT) as f:
        BLINKS = 75
        allStones = [int(x) for x in f.read().split(" ")]
        
        countCache = {}
        def simulateBlink(stone):
            stones = []
            str_stone = str(stone)
            if stone == 0:
                return [1]
            elif len(str_stone) % 2 == 0:
                return [
                    int(str_stone[ : len(str_stone)//2]),
                    int(str_stone[len(str_stone)//2 : ]),
                ]
            else:
                return [stone * 2024]
        
        # Convert initial list to dictionary of counts
        allStones = {x: 1 for x in allStones}
        for i in range(BLINKS):
            new = {}
            start = time.time()
            for stone in allStones:
                newStones = simulateBlink(stone)
                [new.update({s: new.get(s, 0) + allStones.get(stone)}) for s in newStones]
            end = time.time()
            allStones = new
        total = sum(allStones.values())
        print(f'Part 2: {total}')


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')