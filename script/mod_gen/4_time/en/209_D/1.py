def main():
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    cd = [list(map(int, input().split())) for _ in range(Q)]
    # 木構造にグラフを作成
    graph = [[] for _ in range(N)]
    for a, b in ab:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # 根からの距離を求める
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                stack.append(i)
    # 各クエリについて、距離の偶奇で判定
    for c, d in cd:
        if (dist[c-1] + dist[d-1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()