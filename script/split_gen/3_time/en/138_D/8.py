def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    operations = [list(map(int, input().split())) for _ in range(Q)]
    # make adjacency list
    adj_list = [[] for _ in range(N)]
    for e in edges:
        adj_list[e[0]-1].append(e[1]-1)
        adj_list[e[1]-1].append(e[0]-1)
    # make tree
    tree = [0 for _ in range(N)]
    # make parent list
    parent = [-1 for _ in range(N)]
    # make child list
    child = [[] for _ in range(N)]
    # make depth list
    depth = [0 for _ in range(N)]
    # make size list
    size = [0 for _ in range(N)]
    # make depth first search list
    dfs = []
    # make stack
    stack = [0]
    while stack:
        v = stack.pop()
        dfs.append(v)
        for c in adj_list[v]:
            if c == parent[v]:
                continue
            parent[c] = v
            child[v].append(c)
            depth[c] = depth[v] + 1
            stack.append(c)
    # make size list
    for v in reversed(dfs):
        size[v] = 1
        for c in child[v]:
            size[v] += size[c]
    # make tree
    for o in operations:
        tree[o[0]-1] += o[1]
        if o[0] < N:
            tree[o[0]] -= o[1]
    for v in range(1, N):
        tree[v] += tree[parent[v]]
    print(' '.join(map(str, tree)))
