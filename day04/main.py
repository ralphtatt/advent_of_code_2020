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
            return is_valid_byr(passport_details[req])
        if req == 'iyr':
            return is_valid_iyr(passport_details[req])
        if req == 'eyr':
            return is_valid_eyr(passport_details[req])
        if req == 'hgt':
            return is_valid_hgt(passport_details[req])
        if req == 'hcl':
            return is_valid_hcl(passport_details[req])
        if req == 'ecl':
            return is_valid_ecl(passport_details[req])
        if req == 'pid':
            return is_valid_pid(passport_details[req])
    

def is_valid_byr(value):
    return '1920' < value and value < '2020' and len(value) == 4 # No need to convert to int
    
def is_valid_iyr(value):
    return '2010' < value and value < '2020' and len(value) == 4 # No need to convert to int

def is_valid_eyr(value):
    return '2020' < value and value < '2030' and len(value) == 4 # No need to convert to int

def is_valid_hgt(value):
    if len(value) == 4:
        if value[2:4] == 'in':
            if '59' < value[0,2] and value[0,2] < '76':
                return True
    if len(value) == 5:
        if value[3:5] == 'cm':
            if '149' < value[0,3] and value[0,3] < '194':
                return True
    return False

def is_valid_hcl(value):
    return True

def is_valid_ecl(value):
    return True

def is_valid_pid(value):
    return True

valid_passports = sum([1 if is_valid_passport_improved(pp) else 0 for pp in id_list])
print(f'Part two: {valid_passports}')


