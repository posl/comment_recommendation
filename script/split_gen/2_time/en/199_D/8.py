def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**9
    dp = [[INF for _ in range(3)] for _ in range(N+1)]
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 1
    for i in range(2, N+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        dp[i][1] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
    for i in range(M):
        if dp[AB[i][0]][0] == INF:
            print(0)
            return
        elif dp[AB[i][0]][1] == INF:
            print(0)
            return
        elif dp[AB[i][0]][2] == INF:
            print(0)
            return
        elif dp[AB[i][1]][0] == INF:
            print(0)
            return
        elif dp[AB[i][1]][1] == INF:
            print(0)
            return
        elif dp[AB[i][1]][2] == INF:
            print(0)
            return
        elif dp[AB[i][0]][0] == 1 and dp[AB[i][1]][0] == 1:
            print(0)
            return
        elif dp[AB[i][0]][0] == 1 and dp[AB[i][1]][1] == 1:
            print(0)
            return
        elif dp[AB[i][0]][0] == 1 and dp[AB[i][1]][2] == 1:
            print(0)
            return
        elif dp[AB[i][0]][1] == 1 and dp[AB[i][1]][0] == 1:
            print(0)
            return
        elif dp[AB[i][0]][1] == 1 and dp[AB[i][1]][
