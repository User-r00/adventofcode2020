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
    min = line[0]
    max = line[1]
    count = line[3].count(line[2])
    
    # If the count is between the mix and max, save it.
    if count >= min and count <= max:
        valid_passwords += 1
        
print(valid_passwords)