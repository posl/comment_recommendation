def solve(h):
    if h == 1:
        return 1
    else:
        return 1 + 2 * solve(h // 2)

if __name__ == '__main__':
    solve()