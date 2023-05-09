def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    left = -10**18
    right = 10**18
    while right - left > 1:
        mid = (left + right) // 2
        x = 0
        for i in range(N):
            if A[i] < 0:
                j = bisect.bisect_left(A, (mid-1)//A[i])
                x += i - j
            else:
                j = bisect.bisect_right(A, mid//A[i])
                x += N - j
        if x < K:
            left = mid
        else:
            right = mid
    print(right)
