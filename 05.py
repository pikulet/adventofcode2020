with open('05-input', 'r') as f:
    data = f.read().splitlines()

def get_row(frontback):
    return binary_search(frontback, 0, 'F', 127, 'B')

def get_col(leftright):
    return binary_search(leftright, 0, 'L', 7, 'R')

def binary_search(seq, low, LOWCHAR, high, HIGHCHAR):
    for s in seq: 
        mid = (low + high) // 2
        if s == LOWCHAR:
            high = mid
        else:
            low = mid + 1

    return low

def get_seat_id(seat):
    frontback = seat[:7]
    row = get_row(frontback)
    leftright = seat[7:]
    col = get_col(leftright)

    seat_id = row * 8 + col
    return seat_id

seat_ids = set(list(map(get_seat_id, data)))
max_seat_id = max(seat_ids)
min_seat_id = min(seat_ids)

print('Part A:', max_seat_id)

all_seat_ids = set(range(min_seat_id, max_seat_id + 1))
free_seats = all_seat_ids - seat_ids
print('Part B:', free_seats)
