#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 2 part 1."""

# Read puzzle input to a list.
with open('input.py', 'r') as f:
    data = [line.strip() for line in f.readlines()]
    

lines = []
def parse_line(line):
    '''Parse line into min, max, and content.'''
    min_max, char, password = line.split(' ')
    char = char.replace(':', '')
    min, max = min_max.split('-')
    lines.append((int(min), int(max), char, password))
   
for line in data:
    parse_line(line)

valid_passwords = 0
for line in lines:
    # Count how many times a letter appears.
    index1 = line[0] - 1
    index2 = line[1] - 1
    char = line[2]
    password = line[3]
    first_char = password[index1]
    second_char = password[index2]
    
    if first_char != second_char:
        if first_char == char:
            valid_passwords += 1
        elif second_char == char:
            valid_passwords += 1
            
        
print(valid_passwords)
