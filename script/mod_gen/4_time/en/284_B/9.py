def count_odd_numbers(numbers):
    return len(list(filter(lambda x: x % 2 == 1, numbers)))

if __name__ == '__main__':
    count_odd_numbers()