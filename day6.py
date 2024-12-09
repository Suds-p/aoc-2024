import time
INPUT = './inputs/6.input'

def part1():
    with open(INPUT) as f:
        grid = [list(line) for line in f.read().split("\n")]

        # print(f'LENGTH: {len(grid[0])}    HEIGHT: {len(grid)}')
        currPos = None
        for row in grid:
            if '^' in row or 'v' in row or '>' in row or '<' in row:
                guard = '^' if '^' in row else\
                        'v' if 'v' in row else\
                        '>' if '>' in row else '<'
                currPos = (grid.index(row), row.index(guard))
                break

        # Check if position is outside the map
        def reachedEnd(pos):
            return (pos[0] == len(grid) or pos[0] == -1) or \
                   (pos[1] == len(grid[0]) or pos[1] == -1)

        # Go to next position in given direction
        def updatePos(currPos, dirIndex):
            return (currPos[0] + DIRS[dirIndex][0], currPos[1] + DIRS[dirIndex][1])

        # Check if given position has obstacle
        def isObstacle(pos):
            # print(pos)
            return grid[pos[0]][pos[1]] == '#'

        startDirs = {
            '^': 0,
            '>': 1,
            'v': 2,
            '<': 3
        }
        startDirIndex = startDirs[grid[currPos[0]][currPos[1]]]
        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visitCount = 1  # count starting position as well
        while True:
            # Check if current pos was not visited, update count as necessary
            if grid[currPos[0]][currPos[1]] == '.':
                visitCount += 1
            grid[currPos[0]][currPos[1]] = 'X'
            # Get next pos in current direction
            nextPos = updatePos(currPos, startDirIndex)
            # If next pos is off the grid, exit everything
            if reachedEnd(nextPos):
                break
            # If next pos is an obstacle, turn right
            elif isObstacle(nextPos):
                startDirIndex = (startDirIndex + 1) % 4
            else:
                currPos = nextPos

        print(f'Part 1: {visitCount}')


def part2():
    with open(INPUT) as f:
        grid = [list(line) for line in f.read().split("\n")]

        # print(f'LENGTH: {len(grid[0])}    HEIGHT: {len(grid)}')
        guardPos = None
        for row in grid:
            if '^' in row or 'v' in row or '>' in row or '<' in row:
                guard = '^' if '^' in row else\
                        'v' if 'v' in row else\
                        '>' if '>' in row else '<'
                guardPos = (grid.index(row), row.index(guard))
                break

        # Check if position is outside the map
        def reachedEnd(pos):
            return (pos[0] == len(grid) or pos[0] == -1) or \
                   (pos[1] == len(grid[0]) or pos[1] == -1)

        # Go to next position in given direction
        def updatePos(currPos, dirIndex):
            return (currPos[0] + DIRS[dirIndex][0], currPos[1] + DIRS[dirIndex][1])

        # Check if given position has obstacle
        def isObstacle(pos):
            # print(pos)
            return grid[pos[0]][pos[1]] == '#'

        startDirs = {
            '^': 0,
            '>': 1,
            'v': 2,
            '<': 3
        }
        startDirIndex = startDirs[grid[guardPos[0]][guardPos[1]]]
        guardStartDirIndex = startDirIndex
        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        mainTrack = set() # Keep track of guard's entire path
        
        # Trace guard's initial path
        currPos = guardPos
        grid[guardPos[0]][guardPos[1]] = '.'
        while True:
            grid[currPos[0]][currPos[1]] = 'X'
            mainTrack.add(currPos)
            # Get next pos in current direction
            nextPos = updatePos(currPos, startDirIndex)
            # If next pos is off the grid, exit everything
            if reachedEnd(nextPos):
                break
            # If next pos is an obstacle, turn right
            elif isObstacle(nextPos):
                startDirIndex = (startDirIndex + 1) % 4
            else:
                currPos = nextPos

        for p in mainTrack:
            grid[p[0]][p[1]] = '.'

        obstacles = 0
        count = 0
        for point in mainTrack:
            count += 1
            track = []
            currPos = guardPos
            startDirIndex = guardStartDirIndex
            
            # Add as obstacle
            save = grid[point[0]][point[1]]
            grid[point[0]][point[1]] = '#'
            
            # Run through path
            # If has loop, increase counter
            while True:
                # If same position with same direction reached, we did a loop
                if type(grid[currPos[0]][currPos[1]]) == int and grid[currPos[0]][currPos[1]] >= 4:
                    obstacles += 1
                    break
                
                if grid[currPos[0]][currPos[1]] == '.' or type(grid[currPos[0]][currPos[1]]) == int:
                    grid[currPos[0]][currPos[1]] = 0 if grid[currPos[0]][currPos[1]] == '.' else grid[currPos[0]][currPos[1]] + 1
                
                track.append(currPos)
                # Get next pos in current direction
                nextPos = updatePos(currPos, startDirIndex)
                # If next pos is off the grid, exit everything
                if reachedEnd(nextPos):
                    break
                # If next pos is an obstacle, turn right
                elif isObstacle(nextPos):
                    startDirIndex = (startDirIndex + 1) % 4
                else:
                    currPos = nextPos
            
            
            # Reset grid
            grid[point[0]][point[1]] = save
            for p in track:
                grid[p[0]][p[1]] = '.'
        
        print(f'Part 2: {obstacles}')


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')


# 1843 too high