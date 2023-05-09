def sum_num(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
a, b = map(int, input().split())
