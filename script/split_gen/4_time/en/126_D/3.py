def main():
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    color = [None] * (N + 1)
    color[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for u, w in adj[v]:
            if color[u] is None:
                color[u] = color[v] ^ (w % 2)
                stack.append(u)
    print(*color[1:], sep='
')
