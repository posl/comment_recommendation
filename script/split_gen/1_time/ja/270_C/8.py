def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    # グラフ部分
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    # 頂点 X から頂点 Y への単純パスを求める
    # まず頂点 X から頂点 Y へのパスを求める
    path = []
    stack = [X]
    while stack:
        v = stack.pop()
        path.append(v)
        if v == Y:
            break
        for u in graph[v]:
            if u not in path:
                stack.append(u)
    # 頂点 X から頂点 Y への単純パスを求める
    simple_path = [path[0]]
    for i in range(1, len(path)-1):
        if path[i-1] in graph[path[i]] and path[i+1] in graph[path[i]]:
            continue
        simple_path.append(path[i])
    simple_path.append(path[-1])
    print(*simple_path)
