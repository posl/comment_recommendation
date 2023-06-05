def solve(x, m):
    d = int(max(x))
    l = d + 1
    r = 10 ** 18 + 1
    while r - l > 1:
        mid = (l + r) // 2
        if check(x, m, mid):
            l = mid
        else:
            r = mid
    return l - (d + 1) + 1

if __name__ == '__main__':
    solve()