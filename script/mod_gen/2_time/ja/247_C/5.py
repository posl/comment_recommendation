def solve(n):
    if n == 1:
        return [1]
    else:
        return solve(n-1) + [n] + solve(n-1)
N = int(input())
print(*solve(N))
