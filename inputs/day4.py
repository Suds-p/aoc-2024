import time

INPUT_FILE = './inputs/4.input'
XMAS = 'XMAS'


def part1():
    with open(INPUT_FILE) as f:
        grid = f.read().split('\n')
        LENGTH, HEIGHT = len(grid), len(grid[0])

        # List all possible directions
        DIRS = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # down-right
            (1, -1),  # down-left
            (-1, 1),  # up-right
            (-1, -1)  # up-left
        ]

        def inBounds(r, c): return 0 <= r < LENGTH and 0 <= c < HEIGHT

        # Takes in row, col, direction of word search
        def checkForXmas(r, c, d):
            wordExists = True
            for i in range(4):
                row, col = r + i*d[0], c + i*d[1]
                if inBounds(row, col):
                    if XMAS[i] != grid[row][col]:
                        wordExists = False
                        break
                else:
                    wordExists = False
                    break
            return wordExists

        # Scan for Xs
        totalXs = 0
        for row in range(LENGTH):
            for col in range(HEIGHT):
                if grid[row][col] == 'X':
                    for direction in DIRS:
                        totalXs += checkForXmas(row, col, direction)

        print(f'Part 1: {totalXs}')


def part2():
    with open(INPUT_FILE) as f:
        grid = f.read().split('\n')
        LENGTH, HEIGHT = len(grid), len(grid[0])

        # List all possible directions
        DIRS = [
            (1, 1),   # down-right
            (1, -1),  # down-left
            (-1, 1),  # up-right
            (-1, -1)  # up-left
        ]

        def inBounds(r, c): return 0 <= r < LENGTH and 0 <= c < HEIGHT

        def checkForX_mas(r, c):
            wordExists = False
            word = [
                grid[r + DIRS[i][0]][c + DIRS[i][1]] \
                for i in range(4) \
                    if inBounds(r + DIRS[i][0], c + DIRS[i][1])
            ]

            if len(word) == 4:
                if (ord(word[0]) - ord('A') + 1) * (ord(word[3]) - ord('A') + 1) == 247 and \
                   (ord(word[1]) - ord('A') + 1) * (ord(word[2]) - ord('A') + 1) == 247:
                    wordExists = True

            return wordExists

        totalWords = 0
        for row in range(LENGTH):
            for col in range(HEIGHT):
                if grid[row][col] == 'A':
                    totalWords += checkForX_mas(row, col)

        print(f'Part 2: {totalWords}')


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')
