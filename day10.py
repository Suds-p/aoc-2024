import time
INPUT = './inputs/10.input'
# INPUT = "sample"

def printGrid(grid):
    for row in grid:
        print(' '.join(row))

def part1():
    with open(INPUT) as f:
        lines = [list(line) for line in f.read().split("\n")]
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def getNeighbors(row, col):
            neighbors = []
            for dir in dirs:
                r, c = row + dir[0], col + dir[1]
                if 0 <= r < len(lines) and 0 <= c < len(lines[0]):
                    neighbors.append((r, c))
            return neighbors

        # Collect positions of all 9s
        peakNeighbors = []
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                if lines[row][col] == '9':
                    peakNeighbors.append([(row, col)]) # will contain list of nodes in neighborhood of peak

        # Perform BFS from each peak until reaching trailhead
        # printGrid(lines)
        scoreGrid = [['.' for i in range(len(lines))] for j in range(len(lines[0]))]
        
        totalScore = 0
        while True:
            updates = 0
            for i in range(len(peakNeighbors)):
                nodes = peakNeighbors[i]
                if nodes == []:
                    continue
                
                # Go through each node, get all valid neighbors
                allNeighbors = set()
                for node in nodes:
                    row, col = node
                    height = int(lines[row][col])
                    neighbors = getNeighbors(row, col)
                    # Collect neighbors of all nodes so updates will not clash with other neighbors
                    for neighbor in neighbors:
                        if lines[neighbor[0]][neighbor[1]] == str(height - 1):
                            allNeighbors.add(neighbor)
                            updates += 1
                
                # Update scores on neighbors
                for n in allNeighbors:
                    if scoreGrid[n[0]][n[1]] == '.':
                        scoreGrid[n[0]][n[1]] = '1'
                    else:
                        scoreGrid[n[0]][n[1]] = str(int(scoreGrid[n[0]][n[1]]) + 1)
                    
                    if height - 1 == 0:
                        totalScore += 1
                
                # Update neighbor list
                peakNeighbors[i] = list(allNeighbors) if len(allNeighbors) > 0 else None
            
            if updates == 0:
                break

        # printGrid(scoreGrid)
        print(f'Part 1: {totalScore}')


def part2():
    with open(INPUT) as f:
        lines = [list(line) for line in f.read().split("\n")]
        # printGrid(lines)
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def getNeighbors(row, col):
            neighbors = []
            for dir in dirs:
                r, c = row + dir[0], col + dir[1]
                if 0 <= r < len(lines) and 0 <= c < len(lines[0]):
                    neighbors.append((r, c))
            return neighbors
        
        def countTrails(pos):
            height = int(lines[pos[0]][pos[1]])
            if height == 9:
                return 1
            
            ns = getNeighbors(*pos)
            totalCount = 0
            for n in ns:
                if int(lines[n[0]][n[1]]) == height + 1:
                    totalCount += countTrails(n)
            return totalCount
        
        # r, c = 2, 3
        # print(f'Rating for ({r}, {c}) is {countTrails((r, c))}')
        
        trailheads = []
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                if lines[row][col] == '0':
                    trailheads.append((row, col))

        totalRating = 0
        
        for trailhead in trailheads:
            totalRating += countTrails(trailhead)
        
        print(f'Part 2: {totalRating}')


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


# print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')
