import time
INPUT = "5.input"


def part1():
    with open(INPUT) as f:
        lines = f.read().split("\n")

        updateStart = 0
        rules = []
        nums = set()
        for i in range(len(lines)):
            if lines[i] == "":
                updateStart = i+1
                break

            rule = [int(x) for x in lines[i].split("|")]
            rules.append(rule)
            nums.add(rule[0])
            nums.add(rule[1])

        numRank = dict(zip(nums, range(len(nums))))
        adj = [[0 for i in range(len(nums))] for i in range(len(nums))]

        # n^2
        for rule in rules:
            adj[numRank[rule[0]]][numRank[rule[1]]] = 1

        total = 0
        # n*m
        for line in lines[updateStart:]:
            update = [int(x) for x in line.split(",")]

            isUpdateValid = True
            for pageI in range(1, len(update)):
                if adj[numRank[update[pageI-1]]][numRank[update[pageI]]] == 0:
                    isUpdateValid = False
                    break

            if isUpdateValid:
                midnum = int(update[len(update) // 2])
                total += midnum

        print(f'Part 1: {total}')


def part2():
    with open(INPUT) as f:
        lines = f.read().split("\n")

        updateStart = 0
        rules = []
        nums = set()
        for i in range(len(lines)):
            if lines[i] == "":
                updateStart = i+1
                break

            rule = [int(x) for x in lines[i].split("|")]
            rules.append(rule)
            nums.add(rule[0])
            nums.add(rule[1])

        numRank = dict(zip(nums, range(len(nums))))
        adj = [[0 for i in range(len(nums))] for i in range(len(nums))]

        for rule in rules:
            adj[numRank[rule[0]]][numRank[rule[1]]] = 1

        total = 0
        for line in lines[updateStart:]:
            update = [int(x) for x in line.split(",")]

            isUpdateBad = False
            # Bubble sort to fix bad updates
            for pageJ in range(len(update)):
                swaps = 0
                for pageI in range(1, len(update)):
                    if adj[numRank[update[pageI-1]]][numRank[update[pageI]]] == 0:
                        isUpdateBad = True
                        update[pageI-1], update[pageI] = update[pageI], update[pageI-1]
                        swaps += 1
                if swaps == 0:
                    break

            if isUpdateBad:
                midnum = int(update[len(update) // 2])
                total += midnum

        print(f'Part 2: {total}')


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')
