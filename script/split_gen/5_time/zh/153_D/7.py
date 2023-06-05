def solve(h):
    if h == 1:
        return 1
    else:
        return 2 * solve(h // 2) + 1
