def main():
    N, Q = map(int, input().split())
    # N = 6
    # Q = 2
    # a = [1, 1, 2, 3]
    # b = [2, 3, 4, 6]
    # p = [1, 1]
    # x = [10, 10]
    a = [None] * (N - 1)
    b = [None] * (N - 1)
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
    p = [None] * Q
    x = [None] * Q
    for i in range(Q):
        p[i], x[i] = map(int, input().split())
    # グラフを作る
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        graph[a[i] - 1].append(b[i] - 1)
        graph[b[i] - 1].append(a[i] - 1)
    # DFSで頂点の親を求める
    parent = [-1] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if parent[u] == -1:
                parent[u] = v
                stack.append(u)
    # DFSで頂点の子孫を求める
    children = [[] for _ in range(N)]
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if parent[u] == v:
                children[v].append(u)
                stack.append(u)
    # 頂点の親から子孫への加算値を求める
    dp = [0] * N
    for i in range(Q):
        dp[p[i] - 1] += x[i]
    # 頂点の子孫から親への加算値を求める
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if parent[u] == v:
                dp[u] += dp[v]
                stack.append(u)
    # 頂

if __name__ == '__main__':
    main()