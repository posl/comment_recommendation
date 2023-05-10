def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))
