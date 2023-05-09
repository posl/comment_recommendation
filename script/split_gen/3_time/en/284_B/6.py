def count_odd_numbers(n, numbers):
    count = 0
    for i in range(n):
        if numbers[i] % 2 != 0:
            count += 1
    return count
