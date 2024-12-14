import time
INPUT = './inputs/12.input'

def printGrid(grid):
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()

def part1():
    with open(INPUT) as f:
        grid = [list(line) for line in f.read().split("\n")]
        visited = [[False for i in range(len(grid))] for j in range(len(grid[0]))]
        
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
        grid = [list(line) for line in f.read().split("\n")]
        visited = [[False for i in range(len(grid))] for j in range(len(grid[0]))]
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def getNeighbors(row, col):
            neighbors = []
            for dir in dirs:
                r, c = row + dir[0], col + dir[1]
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    neighbors.append((r, c))
            return neighbors

        def applyOffset(pos, off):
            return (pos[0] + off[0], pos[1] + off[1])

        N, E, W, S = (-1, 0), (0, 1), (0, -1), (1, 0)
        NW, NE, SE, SW = (-1, -1), (-1, 1), (1, 1), (1, -1)
        corners = [(W, NW, N), (N, NE, E), (E, SE, S), (S, SW, W)]
        def getCorners(pos):
            nodes = [
                [applyOffset(pos, offset) for offset in corner]
                for corner in corners
            ]
            return nodes
        
        def inBounds(pos):
            return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])
        
        def isType(pos, typ):
            return inBounds(pos) and grid[pos[0]][pos[1]] == typ
        
        # Check that values of surrounding nodes creates a corner
        # Checks for one of the following corner types (root node is bottom right):
        #  . .     . x     x .
        #  . x     x x     . x
        def validateCorner(nodes, t):
            isPlant1, isPlant2, isPlant3 = isType(nodes[0], t), isType(nodes[1], t), isType(nodes[2], t)
            return (not isPlant2 and isPlant1 == isPlant3) or (isPlant2 and (not isPlant1 and not isPlant3))
        
        def countCorners(pos):
            plant = grid[pos[0]][pos[1]]
            total = sum([validateCorner(cornerSet, plant) for cornerSet in getCorners(pos)])
            return total
        
        
        def scanRegion(pos):
            queue = [pos]
            plant = grid[pos[0]][pos[1]]
            area, sides = 1, countCorners(pos)
            
            visited[pos[0]][pos[1]] = True
            while len(queue) > 0:
                newQueue = []
                for node in queue:
                    ns = getNeighbors(*node)
                    for n in ns:
                        if grid[n[0]][n[1]] == plant and not visited[n[0]][n[1]]:
                            newQueue.append(n)
                            visited[n[0]][n[1]] = True
                            area += 1
                            sides += countCorners(n)
                queue = newQueue
            return area, sides
        
        totalPrice = 0
        # Loop over map
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # If found new cell, scan region from there
                if not visited[row][col]:
                    area, sides = scanRegion((row, col))
                    totalPrice += area * sides
        
        print(f'Part 2: {totalPrice}')


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


# print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')