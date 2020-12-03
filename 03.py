TREE = '#'
EMPTY = '.'

# RULE = RIGHT 3 DOWN 1
with open('03-input', 'r') as f:
    area_map = [row[:-1] for row in f.readlines()]
    width = len(area_map[0])
    height = len(area_map)

rules = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

def get_next_x(x, rule):
    return (x + rule) % width

def get_next_y(y, rule):
    return (y + rule)

def is_tree(x, y):
    return area_map[y][x] == TREE

def is_past_bottom(y):
    return y > height - 1

def count_trees(rule_x, rule_y):
    x = 0
    y = 0

    num_trees = 0
    while not is_past_bottom(y):
        if is_tree(x, y):
            num_trees += 1
        x = get_next_x(x, rule_x)
        y = get_next_y(y, rule_y)

    return num_trees

result = 1
for rule_x, rule_y in rules:
    num_trees = count_trees(rule_x, rule_y)
    print('r {rule_x}, d {rule_y}: {num_trees} trees encountered'.format
          (rule_x=rule_x, rule_y=rule_y, num_trees=num_trees))
    result *= num_trees

print('Product of tree count:', result)


