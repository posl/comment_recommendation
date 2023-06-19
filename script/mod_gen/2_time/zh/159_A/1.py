def solve(n,m):
    res = 0
    if n>0:
        res += n * (n-1) // 2
    if m>0:
        res += m * (m-1) // 2
    return res

if __name__ == '__main__':
    solve()