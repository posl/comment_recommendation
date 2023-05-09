def main():
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    pos = list(map(int, input().split()))
    for i in range(8):
        pos[i] -= 1
    pos[8] = -1
    # 0-1 BFS
    dist = [-1] * 9
    dist[0] = 0
    que = [0]
    for i in range(9):
        if pos[i] == 0:
            dist[i] = 0
            que.append(i)
    while que:
        v = que.pop()
        for to in G[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                que.append(to)
    # 頂点 i にコマ j があるときの最短距離
    dp = [[-1] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            dp[j][i] = dist[abs(i - j)]
    # dp[0][i] = i
    # dp[i][j] = j
    # dp[i][j] = dp[i][k] + dp[k][j]
    for k in range(9):
        for i in range(9):
            for j in range(9):
                if dp[i][j] == -1 or (dp[i][k] != -1 and dp[k][j] != -1 and dp[i][j] > dp[i][k] + dp[k][j]):
                    dp[i][j] = dp[i][k] + dp[k][j]
    # dp[0][i] = i
    # dp[i][j] = j
    # dp[i][j] = dp[i][k] + dp[k][j]
    for k in range(9):
        for i in range(9):
            for j in range(9):
                if dp[i][j] == -1 or (dp[i][k] != -1 and dp[k][j]

if __name__ == '__main__':
    main()