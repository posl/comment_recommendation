def f(a, b):
    if a % 2 == 0:
        if b % 2 == 0:
            return a ^ b
        else:
            return (a ^ (b - 1)) ^ (b - 1)
    else:
        if b % 2 == 0:
            return (a - 1) ^ (b ^ (a - 1))
        else:
            return (a - 1) ^ (b - 1)
a, b = map(int, input().split())
print(f(a, b))
