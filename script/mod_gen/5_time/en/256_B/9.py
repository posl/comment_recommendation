def solve(n, a):
    p = 0
    for i in range(n):
        p += a[i] - 1
    return p

if __name__ == '__main__':
    solve()