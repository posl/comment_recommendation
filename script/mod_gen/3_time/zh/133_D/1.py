def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - sum(b) // 2
    return b

if __name__ == '__main__':
    solve()