#!/usr/bin/env python3

import random
import sys

def generate_numbers(filename, count=100000):
    with open(filename, "w") as file:
        for _ in range(count):
            file.write(str(random.randint(1, 1000000)) + '\n')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
            generate_numbers("input.txt", count)
        except ValueError:
            print("The provided argument is not a valid number.")
    else:
        try:
            count = 100000
            generate_numbers("input.txt", count)
        except ValueError:
            print("An error occurred while generating the file.")