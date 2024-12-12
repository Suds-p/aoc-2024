import time
INPUT = './inputs/9.input'

def part1():
    with open(INPUT) as f:
        diskmap = [int(x) for x in list(f.read())]
        memMap = []
        nextFilePos = len(diskmap) - 1
        i = 0

        # Use while loop for better control over indices
        while i < len(diskmap):
            if diskmap[i] == None:
                i += 1
                continue

            # File location, add immediately
            if i % 2 == 0:
                file_ID = i // 2
                memMap.append(f'{diskmap[i]}:{file_ID}')
                diskmap[i] = None
                i += 1
            # Space location, pull in files from the back
            else:
                space = diskmap[i]
                file_ID = nextFilePos // 2
                fileSize = diskmap[nextFilePos]
                if fileSize == None:
                    nextFilePos -= 2
                    break
                if space < fileSize:
                    memMap.append(f'{space}:{file_ID}')
                    diskmap[nextFilePos] = fileSize - space
                    diskmap[i] = None # space is filled
                    i += 1
                elif space > fileSize:
                    memMap.append(f'{fileSize}:{file_ID}')
                    diskmap[nextFilePos] = None # file is moved
                    diskmap[i] = space - fileSize # update remaining space
                    nextFilePos -= 2
                else:
                    memMap.append(f'{space}:{file_ID}')
                    diskmap[i] = None # space is filled
                    diskmap[nextFilePos] = None
                    nextFilePos -= 2
                    i += 1

        # Calculate checksum
        blockPos = 0
        checksum = 0
        for block in memMap:
            length, ID = block.split(":")
            length, ID = int(length), int(ID)
            for i in range(length):
                checksum += ID * blockPos
                blockPos += 1
        print(f'Part 1: {checksum}')


def part2_bad():
    with open(INPUT) as f:
        diskmap = [int(x) for x in list(f.read())]

        def insertSort(x, lst):
            for i in range(len(lst)):
                if x < lst[i]:
                    lst.insert(i, x)
                    return lst
            lst.append(x)
            return lst

        # Track positions of spaces of all sizes and create memory map
        files = [] # Stores tuples of (ID, length)
        spaces = {} # size: [list of positions]
        memMap = []
        posList = []
        for i in range(len(diskmap)):
            if posList == []:
                posList.append(0)
            elif i % 2 == 0:
                posList.append(posList[-1] + diskmap[i-1] + diskmap[i-2])

            if i%2 == 0:
                memMap.extend([i // 2] * diskmap[i])
                files.append((i // 2, diskmap[i]))
            else:
                memMap.extend([None] * diskmap[i])
                spacePos = posList[-1] + diskmap[i-1]
                if diskmap[i] in spaces:
                    spaces[diskmap[i]].append(spacePos)
                else:
                    spaces[diskmap[i]] = [spacePos]

        # Work backwards through the list of files
        for i in range(len(posList) - 1, -1, -1):
            # Analyze next file in line
            fileID, fileSize = files.pop()
            filePos = posList[i]

            bestSpace = fileSize
            for size in range(fileSize, 10):
                if size in spaces and filePos >= spaces[size][0]:
                    if bestSpace not in spaces or spaces[size][0] < spaces[bestSpace][0]:
                        bestSpace = size

            if bestSpace in spaces:
                if filePos >= spaces[bestSpace][0]:
                    newPos = spaces[bestSpace].pop(0)
                    # Clean up
                    if spaces[bestSpace] == []:
                        del spaces[bestSpace]
                    
                    for j in range(fileSize):
                        memMap[newPos + j] = fileID
                        memMap[filePos + j] = None
                    
                    # Track position of leftover space
                    if bestSpace > fileSize:
                        leftoverSpace = bestSpace - fileSize
                        if leftoverSpace in spaces:
                            insertSort(newPos + fileSize, spaces[leftoverSpace])
                        else:
                            spaces[leftoverSpace] = [newPos + fileSize]

        checksum = 0
        for i in range(len(memMap)):
            if memMap[i] != None:
                checksum += memMap[i] * i
        print(f'Part 2: {checksum}')


def part2():
    with open(INPUT) as f:
        diskmap = [int(x) for x in list(f.read())]

        


def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')