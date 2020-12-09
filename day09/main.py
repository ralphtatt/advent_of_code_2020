full_numbers_raw = open('input').read().split('\n')[:-1]
full_numbers = [int(i) for i in full_numbers_raw]


test_numbers = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576
]


num_list = full_numbers
preamble = 25


def detrmine_if_sum_exists(num_list, preamble):
    previous_nums = num_list[-(preamble + 1):-1]
    for i in list(range(preamble)):
        for j in list(range(preamble)):
            if i == j:
                continue
            if previous_nums[i] + previous_nums[j] == num_list[-1]:
                return True
    return False


current_position_to_check = preamble + 1

while detrmine_if_sum_exists(num_list[:current_position_to_check], preamble):
    current_position_to_check += 1

encrpytion_weakness = num_list[:current_position_to_check][-1]

print(f'Part one: {encrpytion_weakness}')

length_to_check = 1
searching = True

while searching:
    length_to_check += 1
    for position in list(range(len(num_list) - length_to_check)):
        check_value = sum(num_list[position:length_to_check + position])
        if check_value == encrpytion_weakness:
            searching = False
            break

minimum = min(num_list[position:position + length_to_check])
maximum = max(num_list[position:position + length_to_check])

print(f'Part two:{minimum + maximum}')
