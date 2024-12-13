import time
INPUT = './inputs/12.input'
# INPUT = 'sample'

def printGrid(grid):
    for row in grid:
        print(' '.join(row))

def part1():
    with open(INPUT) as f:
        grid = [list(line) for line in f.read().split("\n")]
        visited = [[False for i in range(len(grid))] for j in range(len(grid[0]))]
        
        # printGrid(grid)        
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def getNeighbors(row, col):
            neighbors = []
            for dir in dirs:
                r, c = row + dir[0], col + dir[1]
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    neighbors.append((r, c))
            return neighbors
        
        # Marks region as visited and returns (area, perimeter) of region
        def scanRegion(pos):
            queue = [pos]
            plant = grid[pos[0]][pos[1]]
            area, perim = 1, 0
            
            visited[pos[0]][pos[1]] = True
            # print(f'Found {plant} region!', end='')
            while len(queue) > 0:
                newQueue = []
                for node in queue:
                    ns = getNeighbors(*node)
                    for n in ns:
                        if grid[n[0]][n[1]] == plant and not visited[n[0]][n[1]]:
                            newQueue.append(n)
                            visited[n[0]][n[1]] = True
                            area += 1
                        elif grid[n[0]][n[1]] != plant:
                            perim += 1
                    
                    # Add edges against bounds of grid
                    perim += 4 - len(ns)
                
                queue = newQueue
            # print(f'\tA={area}, P={perim}')
            return area, perim
            
        totalPrice = 0
        # Loop over map
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # If found new cell, scan region from there
                if not visited[row][col]:
                    area, perim = scanRegion((row, col))
                    totalPrice += area * perim
        
        print(f'Part 1: {totalPrice}')


def part2():
    with open(INPUT) as f:
        
        print(f'Part 2: {0}')


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


print(f'Part 1 took {clock(part1)} ms to run')
# print(f'Part 2 took {clock(part2)} ms to run')