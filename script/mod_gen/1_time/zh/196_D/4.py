def solve(h, w, a, b):
    if a < 0 or b < 0:
        return 0
    if h == 0 and w == 0:
        return 1
    if h < 0 or w < 0:
        return 0
    if h < 2 and w < 2:
        return 0
    if h < 2:
        return solve(w, h, b, a)
    if w < 2:
        return solve(h, w, a, b)
    if h > w:
        return solve(h-2, w, a-1, b) + solve(h, w-2, a-1, b) + solve(h-1, w-1, a, b-1)
    return solve(h-2, w, a-1, b) + solve(h, w-2, a-1, b) + solve(h-1, w-1, a, b-1) + solve(h-1, w-1, a-1, b)

if __name__ == '__main__':
    solve()