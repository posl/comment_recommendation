def main():
    import sys
    #入力
    readline = sys.stdin.readline
    N, M = map(int, readline().split())
    A = [0]*M
    B = [0]*M
    C = [0]*M
    for i in range(M):
        A[i], B[i], C[i] = map(int, readline().split())
        A[i] -= 1
        B[i] -= 1
    #dijkstra法
    #N:頂点数
    #M:辺の数
    #A,B:辺の始点、終点
    #C:辺のコスト
    #s:始点
    #t:終点
    #k:通っていい頂点の最大番号
    #d:始点sから各頂点への最短距離
    #d[t][k]:始点sから頂点tへの最短距離(ただし、通っていい頂点はs,t,k以下)
    def dijkstra(N, M, A, B, C, s, t, k):
        d = [[float("inf")]*N for _ in range(N)]
        d[s][s] = 0
        for i in range(N):
            for j in range(M):
                if i <= A[j] <= k and i <= B[j] <= k:
                    d[i][B[j]] = min(d[i][B[j]], d[i][A[j]]+C[j])
                    d[i][A[j]] = min(d[i][A[j]], d[i][B[j]]+C[j])
        return d[t][k]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans += dijkstra(N, M, A, B, C, i, j, k)
    print(ans)

if __name__ == '__main__':
    main()