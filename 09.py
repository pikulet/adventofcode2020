from collections import deque

with open('09-input', 'r') as f:
    data = [int(x) for x in f.read().splitlines()]

PREAMBLE_LENGTH = 25
def find_first_invalid():
    preamble = data[:PREAMBLE_LENGTH]

    for index in range(PREAMBLE_LENGTH, len(data)):
        seen_numbers = set()
        seen_numbers.add(data[index - PREAMBLE_LENGTH])

        is_found = False
        for j in range(index - PREAMBLE_LENGTH + 1, index):
            remaining = data[index] - data[j]
            if remaining in seen_numbers:
                is_found = True
                break
            seen_numbers.add(data[j])

        if not is_found:
            return data[index]

invalid_num = find_first_invalid()
print('Part A:', invalid_num)

def find_contig_sum(target):
    left = 0
    current_sum = 0

    for index in range(len(data)):
        current_sum += data[index]
        
        while current_sum > target and left < index:
            current_sum -= data[left]
            left += 1

        if current_sum == target:
            return left, index

left, right = find_contig_sum(invalid_num)
arr = data[left: right + 1]
enc_weakness = min(arr) + max(arr)
print('Part B:', enc_weakness)
