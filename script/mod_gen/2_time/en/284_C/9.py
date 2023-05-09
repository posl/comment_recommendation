def main():
    import sys
    from collections import defaultdict
    import numpy as np
    def dfs(G, v):
        if v in G:
            for vv in G[v]:
                if vv in G:
                    G = dfs(G, vv)
            del G[v]
        return G
    def connected_components(G):
        components = []
        while G:
            v = next(iter(G))
            G = dfs(G, v)
            components.append(v)
        return len(components)
    def input():
        return sys.stdin.readline().rstrip()
    N, M = map(int, input().split())
    G = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    print(connected_components(G))

if __name__ == '__main__':
    main()