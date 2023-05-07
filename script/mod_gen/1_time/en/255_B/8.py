def solve(n, k, a, x, y):
    def ok(r):
        seen = [False] * n
        for i in range(k):
            seen[a[i] - 1] = True
        for i in range(n):
            if seen[i]:
                continue
            for j in range(k):
                if ((x[i] - x[a[j] - 1]) ** 2 + (y[i] - y[a[j] - 1]) ** 2) ** 0.5 <= r:
                    seen[i] = True
                    break
        return all(seen)
    ng = -1
    ok = 10 ** 10
    while abs(ok - ng) > 10 ** -5:
        mid = (ok + ng) / 2
        if ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

if __name__ == '__main__':
    solve()