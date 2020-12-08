#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 8 part 2."""

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
    offset = int(re.findall('\d+', line)[0])

    return Instruction(instruction, operator, offset)

def parse_all_instructions(lines):
    return [convert_instruction_to_class(line) for line in lines]

if __name__ == '__main__':
    data = read_input('input.txt')

    for j in range(len(data)):
        instructions = parse_all_instructions(data)
        ins = instructions[j]

        if ins.instruction == 'jmp':
            ins.instruction = 'nop'
        elif ins.instruction == 'nop':
            ins.instruction = 'jmp'
        else:
            continue

        accumulator = 0

        i = 0

        while i < len(instructions):
            if i == len(instructions) - 1:
                print(f'Accumulator: {accumulator}')
            ins = instructions[i]

            if ins.run == True:
                break

            ins.run = True

            if ins.instruction == 'acc':
                if ins.operator == '+':
                    accumulator += ins.offset
                    i += 1
                else:
                    accumulator -= ins.offset
                    i += 1
            elif ins.instruction == 'jmp':
                if ins.operator == '+':
                    i += ins.offset
                else:
                    i -= ins.offset
            else:
                i += 1
                continue
