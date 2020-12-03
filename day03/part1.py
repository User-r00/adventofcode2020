#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 3 part 1."""

def load_input(input_file):
    """Read input file to a tree map."""
    with open(input_file, 'r') as f:
        return [line.strip() for line in f.readlines()]
        
def read_index(map, x, y):
    """Read a given index from the tree map."""
    
def traverse(map, x_step, y_step):
    """Traverse the map, checking for trees along the way."""
    col = 0
    row = 0
    trees = 0

    # Iterate the tree map
    for line in map:
        print(line)
        col += x_step
        row += y_step
        
        # Exit if we are at the bottom of the slope.
        if row > len(map) - 1:
            print('Reached the bottom of the map!')
            return trees
        
        # print(f'Checking x:{col}, y:{row}')
        
        # print(map[row][col % len(line)])
        
        if map[row][col % len(line)] == '#':
            trees += 1
            
    
    return trees
        

if __name__ == '__main__':
    map = load_input('input.py')
    tree_count = traverse(map, 3, 1)
    print(f'Total trees: {tree_count}')