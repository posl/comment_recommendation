def solve(a, n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % a == 0:
        return 1 + solve(a, n // a)
    else:
        return 1 + solve(a, n - 1)
a, n = map(int, input().split())
print(solve(a, n))
