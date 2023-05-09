def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    #print(graph)
    # 1. 任意の頂点を根とする
    # 2. 根から深さ優先探索で木を構築する
    # 3. 構築した木の葉から根へ向かって、葉から根への最短距離を求める
    # 4. 3で求めた最短距離を用いて、任意の2頂点間の最短距離を求める
    # 2. 根から深さ優先探索で木を構築する
    # この時、親頂点の情報も取得しておく
    parent = [-1] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in graph[v]:
            if parent[u] == -1:
                parent[u] = v
                stack.append(u)
    # 3. 構築した木の葉から根へ向かって、葉から根への最短距離を求める
    # この時、親頂点からの重みも考慮して最短距離を求める
    # また、この最短距離を用いて、任意の2頂点間の最短距離を求める
    # この時、親頂点からの重みも考慮して最短距離を求める
    # また、この最短距離を用いて、任意の2頂点間
