def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    INF = 10**18
    A.append(INF)
    A.append(-INF)
    A.sort()
    for k in K:
        l = 0
        r = N+1
        while r-l > 1:
            m = (l+r)//2
            if A[m] - A[m-1] < k:
                k -= A[m] - A[m-1]
                l = m
            else:
                r = m
        print(A[l] + k)
