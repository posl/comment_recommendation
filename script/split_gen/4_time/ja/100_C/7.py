def count_divide_2(n):
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1
    return count
