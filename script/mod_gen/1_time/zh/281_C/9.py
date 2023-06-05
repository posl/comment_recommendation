def solve(n, t, a):
    t %= sum(a)
    for i in range(n):
        if t < a[i]:
            return i + 1, t
        t -= a[i]

if __name__ == '__main__':
    solve()