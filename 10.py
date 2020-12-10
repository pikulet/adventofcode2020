with open('10-input', 'r') as f:
    data = [int(x) for x in f.read().splitlines()]
    
data.sort()
data.insert(0, 0)

def part_a():
    differences = [0] * 4
    differences[3] += 1
    for index in range(len(data) - 1):
        diff = data[index + 1] - data[index]
        differences[diff] += 1

    result = differences[1] * differences[3]
    return result

def part_b():
    memo_table = [None] * len(data)
    memo_table[-1] = 1

    def helper(n):
        if n >= len(data):
            return 0
        elif memo_table[n] is not None:
            return memo_table[n]
        else:
            result = 0
            for i in range(1, 4):
                if n + i >= len(data):
                    break
                elif data[n + i] - data[n] > 3:
                    break
                result += helper(n + i)

            memo_table[n] = result
            return result

    return helper(0)

print('Part A:', part_a())
print('Part B:', part_b())


