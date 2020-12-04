import re # I hate regex

id_list = open('input').read().split('\n\n')

pp_requirements = [
    'byr',
    'iyr',
    'eyr', 
    'hgt',
    'hcl',
    'ecl',
    'pid'
    ] # cid optional

def is_valid_passport(passport):
    for req in pp_requirements:
        if req not in passport:
            return False
    return True

valid_passports = sum([1 if is_valid_passport(pp) else 0 for pp in id_list])

print(f'Part one: {valid_passports}')

counter = 0
for pp in id_list:
    if not is_valid_passport(pp):
        continue
    if not re.search(r'byr:(19[2-9]\d|200[0-2])(\s|$)', pp):
        continue
    if not re.search(r'iyr:(201\d|2020)(\s|$)',pp):
        continue
    if not re.search(r'eyr:(202\d|2030)(\s|$)',pp):
        continue
    if not re.search(r'hgt:(1[5-9]\dcm|59in|6\din|7[0-6]in)(\s|$)',pp):
        continue
    if not re.search(r'hcl:#[0-9a-f]{6}(\s|$)',pp):
        continue
    if not re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)',pp):
        continue
    if not re.search(r'pid:[0-9]{9}(\s|$)',pp):
        continue
    counter+= 1

print(f'Part two: {counter}')
