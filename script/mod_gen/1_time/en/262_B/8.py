def get_input():
    N, M = map(int, input().split())
    edges = {}
    for _ in range(M):
        u, v = map(int, input().split())
        if not u in edges:
            edges[u] = set()
        if not v in edges:
            edges[v] = set()
        edges[u].add(v)
        edges[v].add(u)
    return N, M, edges

if __name__ == '__main__':
    get_input()