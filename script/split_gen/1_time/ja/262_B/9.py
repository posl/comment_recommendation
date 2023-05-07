def main():
    N, M = map(int, input().split())
    # 二次元配列を初期化
    # 0で初期化される
    # 0: 辺が存在しない
    # 1: 辺が存在する
    edge = [[0 for i in range(N)] for j in range(N)]
    for _ in range(M):
        U, V = map(int, input().split())
        edge[U-1][V-1] = 1
        edge[V-1][U-1] = 1
    #print(edge)
    ans = 0
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if edge[a][b] == 1 and edge[b][c] == 1 and edge[c][a] == 1:
                    ans += 1
    print(ans)
