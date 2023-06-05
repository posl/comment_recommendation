def solve(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 0
    elif a == 0 and b == 0:
        return c
    elif a == 0 and c == 0:
        return b
    elif b == 0 and c == 0:
        return a
    elif a == 0:
        return solve(a, b, c - 1) + 1
    elif b == 0:
        return solve(a - 1, b, c) + 1
    elif c == 0:
        return solve(a, b - 1, c) + 1
    else:
        return solve(a - 1, b, c) * a / (a + b + c) + solve(a + 1, b - 1, c) * b / (a + b + c) + solve(a, b + 1, c - 1) * c / (a + b + c) + 1
