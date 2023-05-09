def solve(h):
    if h == 1:
        return 1
    return 2 * solve(h // 2) + 1
