#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 4 part 1."""

def parse_input(file):
    """Read puzzle input file."""
    with open(file, 'r') as f:
        data = f.read()
    
    return data

def aggregate_passports(data):
    """Split input into a list of passports."""
    return [passport.replace('\n', ' ') for passport in data.split('\n\n')]

def calculate_fields(passport):
    """Calclate passport fields."""
    return [kv.split(':')[0] for kv in passport.split(' ')]
    
if __name__ == '__main__':
    data = parse_input('input.txt')
    
    passport_count = 0

    for passport in aggregate_passports(data):
        kvs = calculate_fields(passport)
        if len(kvs) == 8:
            passport_count += 1
        elif len(kvs) == 7 and 'cid' not in kvs:
            passport_count += 1
            
    print(f'Valid passports: {passport_count}')