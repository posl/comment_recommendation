def main():
    N, Q = map(int, input().split())
    edges = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    children = [[] for i in range(N)]
    parent = [-1 for i in range(N)]
    parent[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edges[v]:
            if parent[u] == -1:
                parent[u] = v
                children[v].append(u)
                stack.append(u)
    counter = [0 for i in range(N)]
    for i in range(Q):
        p, x = map(int, input().split())
        p -= 1
        counter[p] += x
    stack = [0]
    while stack:
        v = stack.pop()
        for u in children[v]:
            counter[u] += counter[v]
            stack.append(u)
    print(*counter)
