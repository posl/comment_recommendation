def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # 隣接行列
    #adj = [[0] * N for _ in range(N)]
    #for _ in range(N - 1):
    #    a, b = map(int, input().split())
    #    adj[a - 1][b - 1] = 1
    #    adj[b - 1][a - 1] = 1
    # 高橋君の街
    C = [0] * Q
    # 青木君の街
    D = [0] * Q
    for i in range(Q):
        c, d = map(int, input().split())
        C[i] = c - 1
        D[i] = d - 1
    # 高橋君の街からの距離
    dist =

if __name__ == '__main__':
    main()