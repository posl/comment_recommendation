def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P_cum = [0]
    for p in P:
        P_cum.append(P_cum[-1] + p)
    ans = 0
    for i in range(K, N+1):
        ans = max(ans, (P_cum[i] - P_cum[i-K]) / 2 + P_cum[i-K])
    print(ans)
