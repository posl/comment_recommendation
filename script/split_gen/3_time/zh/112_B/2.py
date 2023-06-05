def main():
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        routes.append((c, t))
    routes.sort(key=lambda x: x[1])
    # print(routes)
    # if routes[0][1] > T:
    #     print("TLE")
    #     return
    dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
    # print(dp)
    for i in range(1, N + 1):
        for j in range(1, T + 1):
            if routes[i - 1][1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - routes[i - 1][1]] + routes[i - 1][0])
            else:
                dp[i][j] = dp[i - 1][j]
    # print(dp)
    if dp[N][T] == 0:
        print("TLE")
    else:
        print(dp[N][T])
