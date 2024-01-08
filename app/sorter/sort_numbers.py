#!/usr/bin/env python3

def sort_numbers_from_file(filename):
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    numbers.sort()
    return numbers

def save_sorted_numbers_to_file(numbers, filename):
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(f"{number}\n")

if __name__ == "__main__":
    sorted_numbers = sort_numbers_from_file('input.txt')
    save_sorted_numbers_to_file(sorted_numbers, 'sorted.txt')
    print("The numbers were sorted successfully.")
