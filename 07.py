from collections import deque

def parse_rule(rule):
    rule = rule.split(' contain ')
    big_bag = rule[0][:-5]

    contains = dict()
    small_bags = rule[1].split(', ')
    for bag in small_bags:
        if bag.startswith('no'):
            break

        bag = bag.split(' bag')[0]
        number = int(bag[0])
        colour = bag[2:]
        contains[colour] = number

    return big_bag, contains

with open('07-input', 'r') as f:
    data = f.read().splitlines()

colour_map = dict()
reverse_colour_map = dict()

for rule in data:
    big_bag, contains = parse_rule(rule)
    colour_map[big_bag] = contains
    for colour in contains:
        container_colours = reverse_colour_map.get(colour, set())
        container_colours.add(big_bag)
        reverse_colour_map[colour] = container_colours

def part_a():
    can_contain_shiny_gold = reverse_colour_map['shiny gold']
    to_traverse = deque(can_contain_shiny_gold)

    while len(to_traverse) != 0:
        colour = to_traverse.popleft()
        container_colours = reverse_colour_map.get(colour, set())
        for c in container_colours:
            if c not in can_contain_shiny_gold:
                to_traverse.append(c)
        can_contain_shiny_gold.add(colour)

    return len(can_contain_shiny_gold)

def get_num_bags(colour):
    num_bags = 0
    contains = colour_map[colour]
    for c, num in contains.items():
        num_bags += num + (num * get_num_bags(c))

    return num_bags

ans_a = part_a()
print('Part A:', ans_a)

ans_b = get_num_bags('shiny gold')
print('Part B:', ans_b)
