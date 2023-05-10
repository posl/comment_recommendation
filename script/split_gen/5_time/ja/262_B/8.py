def main():
    N, M = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(M)]
    
    #print(N,M)
    #print(uv)
    # まずは隣接リストを作る
    adj = [[False for _ in range(N)] for _ in range(N)]
    for u, v in uv:
        adj[u - 1][v - 1] = True
        adj[v - 1][u - 1] = True
    #print(adj)
    # 頂点を選ぶ
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if not adj[i][j]:
                continue
            for k in range(j + 1, N):
                if adj[i][k] and adj[j][k]:
                    ans += 1
    print(ans)
