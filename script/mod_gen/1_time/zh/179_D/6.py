def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    S = set()
    for i in range(K):
        for j in range(L[i], R[i] + 1):
            S.add(j)
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for j in S:
            if i - j < 1:
                break
            dp[i] += dp[i - j]
            dp[i] %= 998244353
    print(dp[N])

if __name__ == '__main__':
    main()