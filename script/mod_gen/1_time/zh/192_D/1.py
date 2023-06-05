def solve(x, m):
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    d = int(max(x))
    ans = 0
    for i in range(d+1, 10):
        x_ = int(x, i)
        if x_ <= m:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()