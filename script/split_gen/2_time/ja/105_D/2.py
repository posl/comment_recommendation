def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    # 累積和の剰余
    R = [s % M for s in S]
    # 剰余の個数
    cnt = {}
    for r in R:
        if r in cnt:
            cnt[r] += 1
        else:
            cnt[r] = 1
    # 組み合わせの数
    ans = 0
    for c in cnt.values():
        ans += c * (c - 1) // 2
    print(ans)
