def main():
    import sys
    from collections import deque
    from heapq import heappush, heappop
    input = sys.stdin.readline
    N = int(input())
    jump = []
    for i in range(N):
        x, y, p = map(int, input().split())
        jump.append([x, y, p, i])
    jump.sort(key=lambda x:(x[2], -x[0], -x[1]))
    INF = 10**18
    dp = [[INF]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for i in range(N):
        for j in range(i+1, N):
            if jump[i][2]*jump[j][2] >= abs(jump[i][0]-jump[j][0]) + abs(jump[i][1]-jump[j][1]):
                dp[i][j] = 1
                dp[j][i] = 1
    for k in range(N):
        for i in range(N):
            for j in range(i+1, N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                dp[j][i] = dp[i][j]
    ans = INF
    for i in range(N):
        ans = min(ans, dp[i][0])
    print(ans)

if __name__ == '__main__':
    main()