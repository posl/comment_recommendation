def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))
