def main():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    visited = [False] * n
    visited[0] = True
    stack = [0]
    while stack:
        now = stack.pop()
        for nxt in edge[now]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            stack.append(nxt)
    print('Yes' if all(visited) else 'No')
