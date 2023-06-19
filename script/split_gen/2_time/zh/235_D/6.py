def solve(a, n):
    if a % 2 == 0:
        return solve(a//2, n) + 1
    elif a % 5 == 0:
        return solve(a//5, n) + 1
    else:
        return 0
