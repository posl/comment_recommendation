def sum_digits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum
A, B = map(int, input().split())
