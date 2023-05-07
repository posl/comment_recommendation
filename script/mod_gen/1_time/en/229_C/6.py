def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0])
    #print(cheese)
    max_cheese = cheese[-1][0]
    #print(max_cheese)
    dp = [0] * (max_cheese + 1)
    for i in range(N):
        for j in range(max_cheese, -1, -1):
            if j + cheese[i][0] > max_cheese:
                continue
            dp[j + cheese[i][0]] = max(dp[j + cheese[i][0]], dp[j] + cheese[i][0] * cheese[i][1])
    #print(dp)
    ans = 0
    for i in range(len(dp)):
        if W >= i:
            ans = max(ans, dp[i] + (W - i) * dp[-1])
    print(ans)

if __name__ == '__main__':
    main()