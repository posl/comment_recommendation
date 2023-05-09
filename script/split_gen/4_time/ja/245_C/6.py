def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    def check(x):
        cnt = 0
        for i in range(n):
            cnt += bisect.bisect_right(b, x - a[i])
        return cnt >= k
    ok = 0
    ng = 10 ** 18 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
