seat_strings = open('input').read().split('\n')[:-1]

binary_conversion = {
    'F': 0,
    'B': 1,
    'L': 0,
    'R': 1
}


def calculate_row(row_string):
    i = 0
    row_number = 0
    while i < 7:
        row_number += binary_conversion[row_string[i]] * (2 ** (6 - i))
        i += 1
    return row_number


def calculate_col(col_string):
    i = 0
    col_number = 0
    while i < 3:
        col_number += binary_conversion[col_string[i]] * (2 ** (2 - i))
        i += 1
    return col_number


def calculate_id(row_string, col_string):
    return row_string * 8 + col_string


def get_details(seating_string):
    row_string = seating_string[:-3]
    col_string = seating_string[-3:]

    row = calculate_row(row_string)
    col = calculate_col(col_string)
    seat_id = calculate_id(row, col)

    return {
        'row': row,
        'col': col,
        'id': seat_id
    }


seat_details = [get_details(ss) for ss in seat_strings]
seat_ids = [seat['id'] for seat in seat_details]

highest_id = max(seat_ids)

print(f'Part one: {highest_id}')

for _id in list(range(highest_id)):
    if (_id - 1) in seat_ids and (_id + 1) in seat_ids and _id not in seat_ids:
        print(f'Part two: {_id}')
