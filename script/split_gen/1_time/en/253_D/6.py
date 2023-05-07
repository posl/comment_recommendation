def solve(n, a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return (n // a) * (a + b)
    else:
        return (n // a) * (a + b) + (n // b) * b - (n // (a * b)) * b
n, a, b = map(int, input().split())
print(solve(n, a, b))
