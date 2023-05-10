def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 累積和
    for i in range(N - 1):
        A[i + 1] += A[i]
    for i in range(M - 1):
        B[i + 1] += B[i]
    # 机 A から i 冊、机 B から j 冊本を読んだときの合計所要時間の最大値を求める
    ans = 0
    j = M
    for i in range(N + 1):
        if A[i - 1] > K:
            break
        while B[j - 1] > K - A[i - 1]:
            j -= 1
        ans = max(ans, i + j - 1)
    print(ans)
