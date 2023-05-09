def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    # print(G)
    # 頂点 0 を根として木を DFS する
    # 親から子への辺を辿る際に、その辺の重みを親の部分木のサイズとして記録しておく
    # 子から親への辺を辿る際に、その辺の重みを子の部分木のサイズとして記録しておく
    def dfs(v, p):
        for u, w in G[v]:
            if u == p:
                continue
            dfs(u, v)
            size[v] += size[u]
            ans[v] += ans[u] + size[u] * w
    size = [1] * N
    ans = [0] * N
    dfs(0, -1)
    # 頂点 0 を根として木を DFS する
    # 親から子への辺を辿る際に、その辺の重みを親の部分木のサイズとして記録しておく
    # 子から親への辺を辿る際に、その辺の重みを子の部分木のサイズとして記録しておく
    def dfs(v, p):
        for u, w in G[v]:
            if u == p:
                continue
            ans[u] = ans[v] + (N - size[u]) * w - size[u] * w
            dfs(u, v)
    dfs(0, -1)
    print(sum(ans))

if __name__ == '__main__':
    main()