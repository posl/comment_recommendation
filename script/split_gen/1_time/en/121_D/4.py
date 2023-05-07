def solve(a, b):
    if a == b:
        return a
    elif a % 2 == 0 and b % 2 == 1:
        return 1
    elif a % 2 == 1 and b % 2 == 0:
        return 0
    elif a % 2 == 0 and b % 2 == 0:
        return solve(a // 2, b // 2)
    elif a % 2 == 1 and b % 2 == 1:
        return solve(a // 2, b // 2) ^ 1
