def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    
    def is_ok(x):
        cnt = 0
        for i in range(N):
            cnt += bisect.bisect_right(B, x - A[i])
        return cnt >= K
    
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    print(meguru_bisect(10**18, 0) + 1)
