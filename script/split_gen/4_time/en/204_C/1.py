def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
    ans = 0
    for i in range(n):
        visited = [False] * n
        stack = [i]
        while stack:
            v = stack.pop()
            if v == i:
                ans += 1
                break
            if not visited[v]:
                visited[v] = True
                stack.extend(graph[v])
    print(ans)
