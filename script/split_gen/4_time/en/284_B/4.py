def count_odd_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 != 0:
            count += 1
    return count
