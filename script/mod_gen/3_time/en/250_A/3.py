def solve(h, w, r, c):
    if h == 1 and w == 1:
        return 0
    if h == 1 and w != 1:
        return 2
    if h != 1 and w == 1:
        return 2
    if h != 1 and w != 1:
        return 4

if __name__ == '__main__':
    solve()