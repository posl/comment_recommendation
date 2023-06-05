def solve(x, m):
    d = int(max(x))
    n = int(x, d+1)
    cnt = 0
    while n <= m:
        cnt += 1
        n += 1
    return cnt

if __name__ == '__main__':
    solve()