def sort_numbers_from_file(filename):
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    numbers.sort()
    return numbers

if __name__ == "__main__":
    sorted_numbers = sort_numbers_from_file('input.txt')
    for num in sorted_numbers:
        print(num)
