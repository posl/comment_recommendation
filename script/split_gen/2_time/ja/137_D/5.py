def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    #print(AB)
    dp = [0] * (M + 1)
    for i in range(M):
        dp[i + 1] = max(dp[i + 1], dp[i])
        for j in range(N):
            if i + AB[j][0] > M:
                continue
            dp[i + AB[j][0]] = max(dp[i + AB[j][0]], dp[i] + AB[j][1])
    print(dp[M])
