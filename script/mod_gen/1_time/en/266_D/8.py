def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))
    S = sorted(S, key=lambda x: x[0])
    dp = [0] * 5
    for i in range(N):
        t, x, a = S[i]
        dp[x] = max(dp[x], a)
        for j in range(5):
            if j != x:
                dp[j] = max(dp[j], dp[j] + a)
    print(max(dp))

if __name__ == '__main__':
    main()