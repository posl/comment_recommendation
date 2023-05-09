def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
    ans = [None] * n
    ans[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in graph[v]:
            if ans[nv] is None:
                ans[nv] = ans[v] + w % 2
                stack.append(nv)
    print(*[a % 2 for a in ans], sep='
')
