#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 4 part 2."""

import re


def parse_input(file):
    """Read puzzle input file."""
    with open(file, 'r') as f:
        data = f.read()
    
    return data
    
def aggregate_passports(data):
    """Split input into a list of passports."""
    passports = data.split('\n\n')
    return [passport.replace('\n', ' ') for passport in data.split('\n\n')]

def calculate_fields(passport):
    """Calculate passport fields."""
    kvs = passport.split(' ')
    
    p = {}

    for kv in kvs:
        k, v = kv.split(':')
        p[k] = v
    
    return p
    
def validate_kvs(kvs):
    """Validate a passport key value."""
    valid_fields = 0
    
    if 'cid' not in kvs.keys():
        valid_fields += 1

    for k in kvs.keys():
        v = kvs[k]
        if k == 'byr':
            print(f'byr - {v}')
            if len(v) == 4 and int(v) >= 1920 and int(v) <= 2002:
                valid_fields += 1
                print('valid')
        elif k == 'iyr':
            print(f'iyr - {v}')
            if len(v) == 4 and int(v) >= 2010 and int(v) <= 2020:
                valid_fields += 1
                print('valid')
        elif k == 'eyr':
            print(f'eyr - {v}')
            if len(v) == 4 and int(v) >= 2020 and int(v) <= 2030:
                valid_fields += 1
                print('valid')
        elif k == 'hgt':
            print(f'hgt - {v}')
            if 'cm' in v:
                height = int(v.replace('cm', ''))
                if height >= 150 and height <= 193:
                    valid_fields += 1
                    print('valid')
            else:
                height = int(v.replace('in', ''))
                if height >= 59 and height <= 76:
                    valid_fields += 1
                    print('valid')
        elif k == 'hcl':
            print(f'hcl - {v}')
            if len(v) == 7:
                if re.search('#[0-9a-f]{6}', v):
                    valid_fields += 1
                    print('valid')
        elif k == 'ecl':
            print(f'ecl - {v}')
            valid_colors = ['amb',
                            'blu', 
                            'brn',
                            'gry',
                            'grn',
                            'hzl',
                            'oth']
            if v in valid_colors:
                valid_fields += 1
                print('valid')
        elif k == 'pid':
            print(f'pid - {v}')
            if len(v) == 9:
                if re.search('\d{9}', v):
                    valid_fields += 1
                    print('valid')
        elif k == 'cid':
            print(f'cid - {v}')
            print('valid')
            valid_fields += 1
    
    print(valid_fields)    
    if valid_fields == 8:
        print('Valid')
        return True
    print('Invalid')
    return False
            
if __name__ == '__main__':
    data = parse_input('input.txt')
    
    passport_count = 0
    
    for passport in aggregate_passports(data):
        print('\n\n')
        
        kvs = calculate_fields(passport)
        print(f'{kvs}')
        
        if validate_kvs(kvs):
            passport_count += 1
            
    print(f'Valid passports: {passport_count}')
            
 