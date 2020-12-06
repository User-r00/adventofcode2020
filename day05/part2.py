#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 - Day 5 part 2."""

def parse_input(file_name: str):
    with open(file_name, 'r') as f:
        return [[l for l in board_pass.strip()] for board_pass in f.readlines()]

def calculate_seat_id(row, seat):
    return (row * 8) + seat

def find_open_seat(seats):
    possible_seats = []

    for seat in all_seats:
        # Ignore first and last seat
        seat_index = all_seats.index(seat)
        if seat_index == 0:
            continue
        if seat_index == len(all_seats) - 1:
            continue

        # Seats before and after the current seat.
        previous_seat  = all_seats[seat_index - 1]
        next_seat  = all_seats[seat_index + 1]

        # If the previous and next seats dont have an id 1 off from our 
        # current seat save it.
        if previous_seat != seat - 1 or next_seat != seat + 1:
            possible_seats.append(seat)

    # Return the missing seat.
    return possible_seats[1] - 1

if __name__ == '__main__':
    all_seats = []

    for boarding_pass in parse_input('input.txt'):
        rows = [row for row in range(128)]
        seats = [seat for seat in range(8)]

        for instruction in boarding_pass:
            row_length = int(len(rows) / 2)
            seat_length = int(len(seats) / 2)

            if instruction == 'F':
                del rows[row_length:]
            elif instruction == 'B':
                del rows[0:row_length]
            elif instruction == 'L':
                del seats[seat_length:]
            elif instruction == 'R':
                del seats[0:seat_length]

        seat_id = calculate_seat_id(rows[0], seats[0])
        all_seats.append(seat_id)
    
    all_seats.sort()

    open_seat = find_open_seat(all_seats)
    print(f'Seat {open_seat} is open.')
