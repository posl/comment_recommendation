def main():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p - 1] += x
    stack = [0]
    while stack:
        node = stack.pop()
        for child in graph[node]:
            counter[child] += counter[node]
            stack.append(child)
    print(*counter)
