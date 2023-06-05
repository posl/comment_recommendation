def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    return b

if __name__ == '__main__':
    solve()