answers = open('input').read().split('\n\n')

total = sum([len(set(group.replace('\n', ''))) for group in answers])

print(f'Part one: {total}')


def common_character(group):
    split_group = group.split('\n')
    return list(set.intersection(*map(set, split_group)))


total_common = sum([len(common_character(group)) for group in answers])

print(f'Part two: {total_common}')

# For Testing
# [print(f'{group}\n{common_character(group)}\n\n') for group in answers]
