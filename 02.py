with open('02-input', 'r') as f:
    data = f.readlines()

def parse(d):
    d = d.split(':')
    pw = d[1][1:-1]
    policy = d[0]
    letter = policy[-1]
    min_max_val = policy.split()[0].split('-')
    min_val = int(min_max_val[0])
    max_val = int(min_max_val[1])
    return min_val, max_val, letter, pw


def verifyA(min_val, max_val, letter, pw):
    count = pw.count(letter)
    if min_val <= count and count <= max_val:
        return 1
    else:
        return 0

def verifyB(min_val, max_val, letter, pw):
    letter1 = pw[min_val - 1]
    letter2 = pw[max_val - 1]
    if letter1 == letter2:
        return 0
    elif letter1 == letter or letter2 == letter:
        return 1
    else:
        return 0
    
validA = 0
validB = 0

for d in data:
    min_val, max_val, letter, pw = parse(d)
    validA += verifyA(min_val, max_val, letter, pw)
    validB += verifyB(min_val, max_val, letter, pw)

print("Solution for A:", validA)
print("Solution for A:", validB)
