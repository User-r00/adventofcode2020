#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 7 part 1."""

import re

import progressbar

def parse_input(file):
    with open(file, 'r') as f:
        return f.readlines()

def parse_line(line):
    parent = re.findall('^\w+ \w+', line)[0]
    children = re.findall('\d \w+ \w+', line)

    rules = {}

    for child in children:
        qty = int(re.findall('\d', child)[0])
        name = re.findall('[a-zA-Z]+ [a-zA-Z]+', child)[0]

        rules[name] = qty

    return (parent, rules)

def parse_rules(bags):
    rules = {}

    for line in bags:
        rule = parse_line(line)
        rules[rule[0]] = rule[1]

    return rules

def can_contain_gold(rules, bag):
    child_bags = rules[bag]

    if 'shiny gold' in child_bags:
        return True
    else:
        for child in child_bags.keys():
            if can_contain_gold(rules, child):
                return True
    

if __name__ == '__main__':
    bags = parse_input('input.txt')
    rules = parse_rules(bags)

    gold_bags = []

    for bag in progressbar.progressbar(rules.keys()):
        if can_contain_gold(rules, bag):
            gold_bags.append(bag)
        
    num_bags = len(gold_bags)
    print(f'{num_bags} can hold shiny gold bags.')