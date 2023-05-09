def solve(n, m, a, c):
    b = [0] * (m + 1)
    b[0] = c[0] // a[0]
    for i in range(1, m + 1):
        b[i] = (c[i] - sum([b[j] * a[i - j] for j in range(i)])) // a[0]
    return b

if __name__ == '__main__':
    solve()