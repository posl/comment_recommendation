def count_odd_number(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 1:
            count += 1
    return count
