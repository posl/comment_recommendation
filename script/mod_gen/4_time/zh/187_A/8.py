def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
a, b = map(int, input().split())
print(max(sum_digit(a), sum_digit(b)))
