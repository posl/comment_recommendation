def main():
    M = int(input())
    G = [[0] * 9 for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1][v - 1] = 1
        G[v - 1][u - 1] = 1
    P = list(map(int, input().split()))
    # 頂点 1 から頂点 9 への最短距離を求める
    dist = [-1] * 9
    dist[0] = 0
    que = [0]
    while que:
        i = que.pop(0)
        for j in range(9):
            if G[i][j] == 0:
                continue
            if dist[j] != -1:
                continue
            dist[j] = dist[i] + 1
            que.append(j)
    # i 番目のコマが頂点 j に置かれているときの、
    # 頂点 1 から頂点 9 への最短距離の最小値を求める
    dp = [[10 ** 9] * 9 for _ in range(8)]
    dp[0][P[0] - 1] = dist[P[0] - 1]
    for i in range(7):
        for j in range(9):
            for k in range(9):
                if G[j][k] == 0:
                    continue
                dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + dist[k])
    ans = min(dp[7])
    if ans == 10 ** 9:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()