def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = 1 if a[i] else 0
    return b

if __name__ == '__main__':
    solve()