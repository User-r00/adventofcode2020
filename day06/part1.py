#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 6 part 1."""

def parse_input(file):
    with open(file, 'r') as f:
        return f.read()

def get_groups(data):
    return [group for group in data.split('\n\n')]

def get_people(group):
    return [person for person in group.split('\n')]

def count_answers(people):
    answered_questions = []

    for person in people:
        for answer in person:
            if answer not in answered_questions:
                answered_questions.append(answer)
    
    return len(answered_questions)

if __name__ == '__main__':
    data = parse_input('input.txt')
    groups = get_groups(data)

    total_answered_questions = 0

    for group in groups:
        people = get_people(group)
        total_answered_questions += count_answers(people)

    print(f'Total answered questions: {total_answered_questions}')