def solve(n, a, b, c):
    from collections import Counter
    a = Counter(a)
    b = Counter(b)
    c = Counter(c)
    c = [b[c[i]] for i in range(n)]
    return sum([a[i]*c[i] for i in range(n)])

if __name__ == '__main__':
    solve()