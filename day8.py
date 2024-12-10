import time
INPUT = './inputs/8.input'

class color:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'

def printGrid(grid):
    for row in grid:
        print(''.join(row))

def part1():
    with open(INPUT) as f:
        grid = [list(line) for line in f.read().split("\n")]

        def isInBounds(pos):
            row, col = pos
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def calcAntiNode(a, b):
            return (a[0] + 2*(b[0] - a[0]), a[1] + 2*(b[1] - a[1]))

        # Record positions of antennae
        ants = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col]
                if cell != '.':
                    ants.update({cell: ants.get(cell, [])})
                    ants[cell].append((row, col))
        
        nodes = set()
        for freq, pos in ants.items():
            pairs = permutations(pos, r=2)
            for pair in pairs:
                anti = calcAntiNode(*pair)
                if isInBounds(anti):
                    nodes.add(anti)
        
        # Visualize antinodes
        for pos in nodes:
            if grid[pos[0]][pos[1]] == '.':
                grid[pos[0]][pos[1]] = '#'
            grid[pos[0]][pos[1]] = color.OKBLUE + grid[pos[0]][pos[1]] + color.ENDC

        printGrid(grid)

        print(f'Part 1: {len(nodes)}')


def part2():
    with open(INPUT) as f:
        grid = [list(line) for line in f.read().split("\n")]

        def isInBounds(pos):
            row, col = pos
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def calcAntiNodes(a, b):
            nodes = set()
            node = (a[0] + (b[0] - a[0]), a[1] + (b[1] - a[1]))
            while isInBounds(node):
                nodes.add(node)
                node = (node[0] + (b[0] - a[0]), node[1] + (b[1] - a[1]))
            return nodes

        # Record positions of antennae
        ants = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col]
                if cell != '.':
                    ants.update({cell: ants.get(cell, [])})
                    ants[cell].append((row, col))
        
        nodes = set()
        for freq, pos in ants.items():
            pairs = permutations(pos, r=2)
            for pair in pairs:
                nodes = nodes.union(calcAntiNodes(*pair))
        
        # Visualize antinodes
        for pos in nodes:
            if grid[pos[0]][pos[1]] == '.':
                grid[pos[0]][pos[1]] = '#'
            grid[pos[0]][pos[1]] = color.OKGREEN + grid[pos[0]][pos[1]] + color.ENDC

        printGrid(grid)

        print(f'Part 2: {len(nodes)}')



def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')