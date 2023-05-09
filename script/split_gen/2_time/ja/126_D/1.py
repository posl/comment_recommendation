def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    # 深さ優先探索
    # 訪問済みにする
    # 隣接リストを辿っていく
    # 隣接リストが偶数か奇数かで色を変える
    # 隣接リストが偶数か奇数かで色を変える
    # 1: 白
    # 0: 黒
    color = [None] * N
    color[0] = 1
    # 訪問済みにする
    visited = [False] * N
    visited[0] = True
    # 深さ優先探索
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in G[v]:
            if visited[nv]:
                continue
            visited[nv] = True
            if w % 2 == 0:
                color[nv] = color[v]
            else:
                color[nv] = 1 - color[v]
            stack.append(nv)
    for c in color:
        print(c)
main()
