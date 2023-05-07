def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # バケット
    B = [0] * M
    for i in range(N + 1):
        B[S[i] % M] += 1
    # バケットの中の組み合わせ
    ans = 0
    for i in range(M):
        ans += B[i] * (B[i] - 1) // 2
    print(ans)
