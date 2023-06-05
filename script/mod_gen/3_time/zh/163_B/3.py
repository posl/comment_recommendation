def solve(n, m, a):
    if sum(a) < n:
        return -1
    return n - sum(a)

if __name__ == '__main__':
    solve()