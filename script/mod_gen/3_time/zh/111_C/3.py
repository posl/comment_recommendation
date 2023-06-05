def solve(n, v):
    v0 = v[::2]
    v1 = v[1::2]
    c0 = max(v0, key=v0.count)
    c1 = max(v1, key=v1.count)
    if c0 == c1:
        return min(v0.count(c0) + v1.count(c1), v0.count(c0) + v1.count(c1))
    else:
        return len(v0) - max(v0.count(c0), v1.count(c1))

if __name__ == '__main__':
    solve()