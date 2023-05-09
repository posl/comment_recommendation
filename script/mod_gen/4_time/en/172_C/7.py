def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 累積和をとる
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]
    # 二分探索
    ans = 0
    for i in range(N):
        if A[i] > K:
            break
        l = 0
        r = M
        while l < r:
            m = (l+r)//2
            if A[i] + B[m] <= K:
                l = m+1
            else:
                r = m
        ans = max(ans, i+1+l)
    for i in range(M):
        if B[i] > K:
            break
        l = 0
        r = N
        while l < r:
            m = (l+r)//2
            if B[i] + A[m] <= K:
                l = m+1
            else:
                r = m
        ans = max(ans, i+1+l)
    print(ans)

if __name__ == '__main__':
    main()