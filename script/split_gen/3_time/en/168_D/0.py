def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 1から各頂点への最短距離を求める
    dist = [float('inf')] * N
    dist[0] = 0
    for i in range(M):
        if A[i] == 1:
            dist[B[i]-1] = 1
        elif B[i] == 1:
            dist[A[i]-1] = 1
    # 1から各頂点への最短経路の次の頂点を求める
    next = [-1] * N
    for i in range(M):
        if dist[A[i]-1] == dist[B[i]-1] - 1:
            next[B[i]-1] = A[i]
        elif dist[B[i]-1] == dist[A[i]-1] - 1:
            next[A[i]-1] = B[i]
    # 1から各頂点への最短経路を求める
    path = [-1] * N
    path[0] = 1
    for i in range(1, N):
        if path[i] == -1:
            path[i] = next[i]
            while path[i] != 1:
                path[i] = next[path[i]-1]
    # 出力
    print('Yes')
    for i in range(1, N):
        print(path[i])
