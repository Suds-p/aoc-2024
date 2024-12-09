import time
INPUT = './inputs/7.input'

def part1():
    with open(INPUT) as f:
        lines = f.read().split("\n")

        total = 0
        for line in lines:
            answer, elems = line.split(": ")
            answer = int(answer)
            elems = elems.split(" ")

            # Loop up through binary numbers
            N = len(elems) - 1
            for i in range(2 ** N):
                binary = bin(i)[2:].rjust(N, '0')

                # Translate binary to sequence of operators
                # 0 = +, 1 = *
                binary = binary.translate({ord('0'): ord('+'), ord('1'): ord('*')})

                # Combine nums and operators to make expression
                result = elems[0]
                for op in zip(binary, elems[1:]):
                    result = eval(f'{result} {op[0]} {op[1]}')

                if answer == result:
                    total += answer
                    break
        
        print(f'Part 1: {total}')


def part2():
    def evalNums(answer, elems):  
        # Termination: no elements left and answer is smallest possible result
        if len(elems) == 0:              
            return answer == '' or int(answer) == 0 or int(answer) == 1
        elif answer == '':
            return False

        res1 = False if int(answer) % int(elems[-1]) != 0 else evalNums(int(answer) // int(elems[-1]), elems[:-1])
        res2 = False if int(answer) - int(elems[-1]) < 0 else evalNums(int(answer) - int(elems[-1]), elems[:-1])

        if str(answer).endswith(elems[-1]):
            res3 = evalNums(str(answer)[:-len(elems[-1])], elems[:-1])
        else:
            res3 = False

        return res1 or res2 or res3

    with open(INPUT) as f:
        lines = f.read().split("\n")

        total = 0
        for line in lines:
            answer, elems = line.split(": ")
            elems = elems.split(" ")
                
            if evalNums(answer, elems):
                total += int(answer)
        print(f'Part 2: {total}')



def clock(f):
    start = time.time()
    f()
    end = time.time()
    return round((end - start) * 1000, 3)


# print(f'Part 1 took {clock(part1)} ms to run')
print(f'Part 2 took {clock(part2)} ms to run')