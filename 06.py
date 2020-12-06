import functools

with open('06-input', 'r') as f:
    data = f.read().split('\n\n')

def num_qn_a(group_data):
    qns = set(group_data)
    qns.discard('\n')
    return len(qns)

def num_qn_b(group_data):
    return len(list(functools.reduce(lambda x, y: x.intersection(y), 
                                     map(set, group_data.split())))

ans_a = sum(list(map(num_qn_a, data)))
print('Part A:', ans_a)

ans_b = sum(list(map(num_qn_b, data)))
print('Part B:', ans_b)
