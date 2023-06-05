def solve(X,M):
    d = int(max(X)) # X中最大的数字
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    # 二分查找
    l = d+1
    r = 10**18+1
    while l < r:
        m = (l+r)//2
        if check(X,M,m):
            l = m + 1
        else:
            r = m
    return l - d - 1

if __name__ == '__main__':
    solve()