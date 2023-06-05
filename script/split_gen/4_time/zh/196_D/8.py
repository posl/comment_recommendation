def solve(h, w, a, b):
    if a == 0:
        return 1
    elif a < 0:
        return 0
    elif h == 0 or w == 0:
        return 0
    else:
        return solve(h - 1, w, a - 2, b) + solve(h, w - 1, a - 1, b) + solve(h - 2, w, a - 2, b) + solve(h, w - 2, a - 2, b)
h, w, a, b = map(int, input().split())
print(solve(h, w, a, b))
