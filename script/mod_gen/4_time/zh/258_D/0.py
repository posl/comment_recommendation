def solve(n, x, ab):
    a = []
    b = []
    for i in range(n):
        a.append(ab[i][0])
        b.append(ab[i][1])
    s = sum(a)
    t = sum(b)
    c = [2 * a[i] + b[i] for i in range(n)]
    c.sort()
    if s <= x:
        return n * (s + t)
    else:
        i = 0
        while i < n:
            if c[i] > x:
                break
            i += 1
        if i == n:
            return (n - 1) * x + t
        else:
            return i * x + (n - i) * (x + t)

if __name__ == '__main__':
    solve()