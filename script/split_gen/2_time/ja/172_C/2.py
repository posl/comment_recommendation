def main():
    # 入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 累積和
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]
    # 二分探索
    ans = 0
    j = M
    for i in range(N+1):
        if i == N:
            t = K
        else:
            t = K - A[i]
        if t < 0:
            continue
        while j > 0 and B[j-1] > t:
            j -= 1
        ans = max(ans, i+j)
    # 出力
    print(ans)
