def main():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    used = [False] * n
    used[0] = True
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if used[u]:
                continue
            used[u] = True
            stack.append(u)
    print("Yes" if all(used) else "No")
