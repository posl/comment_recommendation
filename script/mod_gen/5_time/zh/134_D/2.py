def solve(n, a):
    b = [0] * (n + 1)
    for i in range(n, 0, -1):
        s = sum(b[i::i]) % 2
        if s != a[i-1]:
            b[i] = 1
    return [i for i, x in enumerate(b) if x]

if __name__ == '__main__':
    solve()