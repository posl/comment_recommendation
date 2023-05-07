def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    # ワーシャルフロイド法
    # 重み付きグラフの全頂点間最短路を求める
    # https://ja.wikipedia.org/wiki/%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95
    # 頂点番号は 0 から始まることに注意
    INF = 10 ** 9 + 7
    d = [[INF] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for i in range(M):
        d[A[i] - 1][B[i] - 1] = C[i]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if d[i][j] == d[i][k] + d[k][j]:
                    ans += d[i][j]
                    break
    print(ans)

if __name__ == '__main__':
    solve()