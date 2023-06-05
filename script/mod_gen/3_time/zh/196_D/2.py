def solve(h, w, a, b):
    if a == 0 and b == 0:
        return 1
    if a < 0 or b < 0:
        return 0
    if h == 1:
        return solve(w, h, b, a)
    if w == 1:
        return solve(h, w, a, b)
    if a == 0:
        return solve(h-1, w, a, b-1)
    return solve(h-1, w, a, b-1) + solve(h-2, w, a-1, b)
h, w, a, b = map(int, input().split())
print(solve(h, w, a, b))
