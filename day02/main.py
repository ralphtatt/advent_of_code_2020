list = open('input').read().split('\n')[:-1]


def password_valid(data):
    data = data.split()
    oc_min = int(data[0].split('-')[0])
    oc_max = int(data[0].split('-')[-1])
    target_letter = data[1][0]
    password = data[2]
    occurences = 0
    for letter in password:
        if letter == target_letter:
            occurences += 1
    return occurences >= oc_min and occurences <= oc_max


def new_password_valid(data):
    data = data.split()
    f_pos = int(data[0].split('-')[0])
    l_pos = int(data[0].split('-')[-1])
    target_letter = data[1][0]
    password = data[2]
    # XOR gate for password aka (OR AND NAND)
    A = password[f_pos - 1] == target_letter
    B = password[l_pos - 1] == target_letter
    return (A or B) and not (A and B)


print(f'Part one: {sum([1 if password_valid(row) else 0 for row in list])}')
print(
    f'Part two: {sum([1 if new_password_valid(row) else 0 for row in list])}')
