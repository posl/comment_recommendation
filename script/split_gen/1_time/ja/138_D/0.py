def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
    visited = [False] * N
    stack = [(0, 0)]
    visited[0] = True
    while stack:
        v, p = stack.pop()
        counter[v] += p
        for w in G[v]:
            if visited[w]:
                continue
            stack.append((w, counter[v]))
            visited[w] = True
    print(*counter)
