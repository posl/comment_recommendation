def solve(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 4
    if n % 2 == 0:
        return solve(n+1)
    else:
        return solve(n-1)
