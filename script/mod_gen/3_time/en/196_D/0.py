def solve(h, w, a, b):
    if a == 0 or b == 0:
        return 1
    return solve(h, w, a - 1, b) + solve(h, w, a, b - 1)
h, w, a, b = map(int, input().split())
print(solve(h, w, a, b))
