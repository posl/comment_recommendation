def sum_digits(integer):
    sum = 0
    while integer:
        sum += integer % 10
        integer //= 10
    return sum
a, b = map(int, input().split())
