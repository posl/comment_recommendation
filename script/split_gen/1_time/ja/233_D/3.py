def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0]
    for i in range(N):
        S.append(S[-1] + A[i])
    # 累積和の値の出現回数
    ans = 0
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        ans += d[S[i] - K]
        d[S[i]] += 1
    print(ans)
