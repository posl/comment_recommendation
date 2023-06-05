def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    left = -10**18
    right = 10**18
    while left + 1 < right:
        mid = (left + right) // 2
        #print(left, mid, right)
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                l = -1
                r = N
                while l + 1 < r:
                    m = (l + r) // 2
                    if A[i] * A[m] <= mid:
                        r = m
                    else:
                        l = m
                cnt += N - r
            else:
                l = -1
                r = N
                while l + 1 < r:
                    m = (l + r) // 2
                    if A[i] * A[m] <= mid:
                        l = m
                    else:
                        r = m
                cnt += r
            if A[i] * A[i] <= mid:
                cnt -= 1
        cnt = cnt // 2
        #print(cnt)
        if cnt < K:
            left = mid
        else:
            right = mid
    print(right)
solve()
