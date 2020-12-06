#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 5 part 1."""

def parse_input(file_name: str):
    with open(file_name, 'r') as f:
        return [[l for l in board_pass.strip()] for board_pass in f.readlines()]

def calculate_seat_id(row, seat):
    return (row * 8) + seat

if __name__ == '__main__':
    all_seats = []
    for boarding_pass in parse_input('input.txt'):
        rows = [row for row in range(128)]
        seats = [seat for seat in range(8)]

        for instruction in boarding_pass:
            row_length = int(len(rows) / 2)
            seat_length = int(len(seats) / 2)

            if instruction == 'F':
                # Remove back half of rows.
                del rows[row_length:]
            elif instruction == 'B':
                # Remove front half of rows.
                del rows[0:row_length]
            elif instruction == 'L':
                del seats[seat_length:]
            elif instruction == 'R':
                del seats[0:seat_length]

        seat_id = calculate_seat_id(rows[0], seats[0])
        all_seats.append(seat_id)
    
    all_seats.sort()
    print(all_seats)
    highest_seat_id = all_seats[len(all_seats) - 1]
    print(f'Highest seat id: {highest_seat_id}')