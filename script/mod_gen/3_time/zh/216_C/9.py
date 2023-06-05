def solve(n):
    if n == 1:
        return 'A'
    if n % 2 == 0:
        return solve(n // 2) + 'B'
    else:
        return solve(n - 1) + 'A'
n = int(input())
print(solve(n))
