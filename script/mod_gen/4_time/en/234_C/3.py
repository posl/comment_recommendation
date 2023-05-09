def solve(k):
    if k == 1:
        return 2
    else:
        return 10 * solve(k - 1) + 2

if __name__ == '__main__':
    solve()