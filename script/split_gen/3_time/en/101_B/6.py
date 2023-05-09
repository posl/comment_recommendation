def sum_digits(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum
