def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 累積和
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]
    # 答え
    ans = 0
    # A から i 冊読む
    for i in range(N+1):
        # A から i 冊読むのにかかる時間
        a = A[i-1] if i > 0 else 0
        # A から i 冊読んで残りの時間で B から読める冊数
        b = 0 if K < a else len(B) - bisect.bisect_right(B, K - a)
        ans = max(ans, i + b)
    print(ans)
