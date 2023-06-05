def solve(n, t, c, ti):
    res = t
    for i in range(n):
        if ti[i] <= t:
            res = min(res, c[i])
    if res == t:
        return "TLE"
    else:
        return res

if __name__ == '__main__':
    solve()