def main():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        counter[p] += x
    stack = [(0, 0)]
    while stack:
        v, p = stack.pop()
        counter[v] += counter[p]
        for u in graph[v]:
            if u == p:
                continue
            stack.append((u, counter[v]))
    print(*counter)
