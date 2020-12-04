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

eye_colours = [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
        ]

def passport_dictionairyfied(passport):
    detail_list = passport.split()
    detail_dict = {}
    for cred in detail_list:
        pair = cred.split(':')
        detail_dict[pair[0]] = pair[1]
    return detail_dict
    
def is_valid_passport_improved(passport):
    passport_details = passport_dictionairyfied(passport)
    for req in pp_requirements:
        if req not in passport:
            return False
        if req == 'byr':
            if not is_valid_byr(passport_details[req]):
                return False
        if req == 'iyr':
            if not is_valid_iyr(passport_details[req]):
                return False
        if req == 'eyr':
            if not is_valid_eyr(passport_details[req]):
                return False
        if req == 'hgt':
            if not is_valid_hgt(passport_details[req]):
                return False
        if req == 'hcl':
            if not is_valid_hcl(passport_details[req]):
                return False
        if req == 'ecl':
            if not is_valid_ecl(passport_details[req]):
                return False
        if req == 'pid':
            if not is_valid_pid(passport_details[req]):
                return False
    

def is_valid_byr(value):
    return '1920' < value and value < '2020' and len(value) == 4 # No need to convert to int
    
def is_valid_iyr(value):
    return '2010' < value and value < '2020' and len(value) == 4 # No need to convert to int

def is_valid_eyr(value):
    return '2020' < value and value < '2030' and len(value) == 4 # No need to convert to int

def is_valid_hgt(value):
    if len(value) == 4:
        if value[2:4] == 'in':
            if '59' <= value[0:2] and value[0:2] <= '76':
                return True
    if len(value) == 5:
        if value[3:5] == 'cm':
            if '150' <= value[0:3] and value[0:3] <= '193':
                return True
    return False

def is_valid_hcl(value):
    return re.search(r'#[0-9a-f]{6}', value) and len(value) == 7

def is_valid_ecl(value):
    return value in eye_colours

def is_valid_pid(value):
    return re.search(r'[0-9]{9}', value)

valider_passports = sum([1 if is_valid_passport_improved(pp) else 0 for pp in id_list])
print(f'Part two: {valider_passports}')


