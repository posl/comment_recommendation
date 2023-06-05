def solve(N, d):
    d.sort()
    dif = d[N//2] - d[N//2-1]
    return dif

if __name__ == '__main__':
    solve()