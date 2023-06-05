def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10 ** 9 + 1
    for a in A:
        ok = -1
        ng = M
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if B[mid] >= a:
                ng = mid
            else:
                ok = mid
        ans = min(ans,abs(a - B[ng]))
        if ng + 1 < M:
            ans = min(ans,abs(a - B[ng + 1]))
    print(ans)
solve()
