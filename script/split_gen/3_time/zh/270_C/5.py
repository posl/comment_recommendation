def input():
    N, X, Y = map(int, input().split())
    tree = [[] for i in range(N)]
    for i in range(N-1):
        U, V = map(int, input().split())
        tree[U-1].append(V-1)
        tree[V-1].append(U-1)
    return N, X-1, Y-1, tree
