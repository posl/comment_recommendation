def count_divide_by_2(num):
    count = 0
    while num % 2 == 0:
        num = num // 2
        count += 1
    return count
