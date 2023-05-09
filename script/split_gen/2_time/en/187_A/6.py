def sum_digits(n):
    return sum(int(c) for c in str(n))
a, b = map(int, input().split())
a = sum_digits(a)
b = sum_digits(b)
print(a if a >= b else b)
