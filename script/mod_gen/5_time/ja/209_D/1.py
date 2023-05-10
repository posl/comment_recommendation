def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    # 隣接リストを作る
    graph = [[] for _ in range(N)]
    for a, b in AB:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # 各頂点の深さを記録する配列
    depth = [-1] * N
    # 根の頂点の深さを 0 にする
    depth[0] = 0
    # 根の頂点を記録する変数
    root = 0
    # 根の頂点から DFS を行う
    stack = [root]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if depth[j] == -1:
                depth[j] = depth[i] + 1
                stack.append(j)
    # 各頂点の親を記録する配列
    parent = [-1] * N
    # 根の頂点の親を -1 にする
    parent[root] = -1
    # 根の頂点から DFS を行う
    stack = [root]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if parent[j] == -1:
                parent[j] = i
                stack.append(j)
    # 高橋君と青木君の街の頂点番号をそれぞれ c, d とする
    for c, d in CD:
        c -= 1
        d -= 1
        # 高橋君の街から根の頂点までの経路を記録する配列
        path_c = []
        i = c
        while i != -1:
            path_c.append(i)
            i = parent[i]
        # 青木君の街から根の頂点まで

if __name__ == '__main__':
    main()