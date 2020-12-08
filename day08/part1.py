#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 8 part 1."""

import re

class Instruction():
    def __init__(self, instruction, operator, offset):
        self.instruction = instruction
        self.operator = operator
        self.offset = offset
        self.run = False

def read_input(file):
    with open(file, 'r') as f:
        return f.readlines()

def convert_instruction_to_class(line):
    instruction = re.findall('[a-z]+', line)[0]
    operator = re.findall('[+-]', line)[0]
    offset = int(re.findall('\d', line)[0])

    return Instruction(instruction, operator, offset)

def parse_all_instructions(lines):
    return [convert_instruction_to_class(line) for line in lines]

if __name__ == '__main__':
    data = read_input('input.txt')
    instructions = parse_all_instructions(data)

    accumulator = 0

    for i in range(len(instructions)):
        ins = instructions[i]
        # print(f'ins: {ins}')

        if ins.run == True:
            print(f'Instruction already run.')
            break

        print(f'{ins.instruction} {ins.operator} {ins.offset} {ins.run}')

        ins.run = True

        if ins.instruction == 'acc':
            if ins.operator == '+':
                print(f'ADDING {ins.offset} TO ACCUMULATOR')
                accumulator += ins.offset
            else:
                print(f'SUBTRACTING {ins.offset} FROM ACCUMULATOR')
                accumulator -+ ins.offset
        elif ins.instruction == 'jmp':
            if ins.operator == '+':
                print(f'MOVING INDEX FORWARD {ins.offset} INSTRUCTIONS')
                i += ins.offset
            else:
                print(f'MOVING INDEX backward {ins.offset} INSTRUCTIONS')
                i -= ins.offset
        else:
            print(f'NOOP')
            continue

    print(f'Accumulator: {accumulator}')