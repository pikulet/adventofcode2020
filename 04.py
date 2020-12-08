import string

def parse_passport(d):
    passport = dict()

    fields = d.split()
    for f in fields:
        f_id, f_value = f.split(":")
        passport[f_id] = f_value

    return passport
    
with open('04-input', 'r') as f:
    data = f.read().split('\n\n')
    all_passports = list(map(parse_passport, data))

def byr_validation(byr):
    byr = int(byr)      # if error, false
    return byr >= 1920 and byr <= 2002

def iyr_validation(iyr):
    iyr = int(iyr)      # if error, false
    return iyr >= 2010 and iyr <= 2020

def eyr_validation(eyr):
    eyr = int(eyr)      # if error, false
    return eyr >= 2020 and eyr <= 2030 

def hgt_validation(hgt):
    if len(hgt) < 3:
        return False

    unit = hgt[-2:]
    value = int(hgt[:-2]) # if error, false
    if unit == 'cm':
        return value >= 150 and value <= 193
    elif unit == 'in':
        return value >= 59 and value <= 76
    else:
        return False

def hcl_validation(hcl):
    if len(hcl) != 7:
        return False
    elif hcl[0] != '#':
        return False

    return all(c in string.hexdigits for c in hcl[1:])

ALLOWED_ECL = { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" }
def ecl_validation(ecl):
    return ecl in ALLOWED_ECL

def pid_validation(pid):
    if len(pid) != 9:
        return False
    return pid.isdigit()

required = {
    "byr"   :   byr_validation,
    "iyr"   :   iyr_validation,
    "eyr"   :   eyr_validation,
    "hgt"   :   hgt_validation,
    "hcl"   :   hcl_validation,
    "ecl"   :   ecl_validation,
    "pid"   :   pid_validation
}
#cid

def is_valid_passport_a(p):
    for r in required:
        if r not in p:
            return False

    return True

def is_valid_passport_b(p):
    for f_id in required:
        if f_id not in p:
            return False

        value = p[f_id]
        rule = required[f_id]
        if not rule(value):
            return False

    return True

num_valid_passports_a = len(list(filter(is_valid_passport_a, all_passports)))
print("Solution for A:", num_valid_passports_a)

num_valid_passports_b = len(list(filter(is_valid_passport_b, all_passports)))
print("Solution for B:", num_valid_passports_b)

