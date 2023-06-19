def solve(a, b):
    if a >= 13:
        return b
    elif a >= 6:
        return b//2
    else:
        return 0
a, b = map(int, input().split())
print(solve(a, b))
