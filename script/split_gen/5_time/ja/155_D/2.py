def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    INF = 10**18
    left = -INF
    right = INF
    while left + 1 < right:
        x = (left + right) // 2
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                l = -1
                r = N
                while l + 1 < r:
                    m = (l + r) // 2
                    if A[m] * A[i] < x:
                        r = m
                    else:
                        l = m
                cnt += N - r
            else:
                l = -1
                r = N
                while l + 1 < r:
                    m = (l + r) // 2
                    if A[m] * A[i] < x:
                        l = m
                    else:
                        r = m
                cnt += r
            if A[i] * A[i] < x:
                cnt -= 1
        cnt //= 2
        if cnt < K:
            left = x
        else:
            right = x
    print(left)
