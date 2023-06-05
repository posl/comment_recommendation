def solve(n, m, a):
    a = sorted(a, reverse = True)
    i = 0
    while i < m and a[i] >= a[0] / (2 ** (i + 1)):
        i += 1
    return sum(a[i:]) + sum([a[0] / (2 ** (i + 1)) for i in range(i)])

if __name__ == '__main__':
    solve()