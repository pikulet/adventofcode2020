import copy

with open('11-test', 'r') as f:
    data = [list(x) for x in f.read().splitlines()]

WIDTH = len(data[0])
HEIGHT = len(data)

FLOOR = '.'
OCCUPIED = '#'
EMPTY = 'L'
OUT_OF_BOUNDS = 'x'

adj_rules = [
    (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1) ]

def get_seat_status(row, col, src):
    if row < 0 or row >= HEIGHT or col < 0 or col >= WIDTH:
        return OUT_OF_BOUNDS
    else:
        return src[row][col]

def rule_adj(row, col, src):
    result = 0
    for rule in adj_rules:
        s = get_seat_status(row + rule[0], col + rule[1], src)
        if s == OCCUPIED:
            result += 1

    return result

def rule_visible(row, col, src):
    result = 0

    for rule in adj_rules:
        index = 1
        while 1:
            s = get_seat_status(row + index * rule[0], col + index * rule[1],
                                src)
            if s == OCCUPIED:
                result += 1
                break
            elif s == OUT_OF_BOUNDS:
                break

            index += 1

    if row == 0 and col == 8:
        print(result)
    return result


def print_map_debug(src):
    print('Printing current map...')
    for row in src:
        print(row)

def run_simulation(enter_rule, leave_rule, data, EMPTY_LIMIT, OCCUPY_LIMIT):
    src = copy.deepcopy(data)
    target = copy.deepcopy(data)

    is_change_made = True

    while is_change_made:
        is_change_made = False

        for row in range(HEIGHT):
            for col in range(WIDTH):
                if src[row][col] == FLOOR:
                    continue
            
                elif src[row][col] == EMPTY and enter_rule(row, col, src) <= EMPTY_LIMIT:
                    target[row][col] = OCCUPIED
                    is_change_made = True
                    continue

                elif src[row][col] == OCCUPIED and leave_rule(row, col, src) >= OCCUPY_LIMIT:
                    target[row][col] = EMPTY
                    is_change_made = True
                    continue

        src = copy.deepcopy(target)
        print_map_debug(src)

    return sum(map(lambda row: 
                   len(list(filter(lambda seat: seat == OCCUPIED, row))), src))

print('Part A:', run_simulation(rule_adj, rule_adj, data, 0, 4))
#print('Part B:', run_simulation(rule_adj, rule_visible, data, 0, 5))

