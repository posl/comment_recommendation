def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # Sのmod Mでの累積和
    SS = [0] * (N + 1)
    for i in range(N + 1):
        SS[i] = S[i] % M
    # SSの各要素の個数
    SS_cnt = [0] * M
    for i in range(N + 1):
        SS_cnt[SS[i]] += 1
    # SSの各要素の個数から組み合わせを計算
    ans = 0
    for i in range(M):
        ans += SS_cnt[i] * (SS_cnt[i] - 1) // 2
    print(ans)
