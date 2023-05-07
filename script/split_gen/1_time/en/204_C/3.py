def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N * N)
        return
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
    ans = 0
    for i in range(N):
        stack = [i]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for next_node in graph[node]:
                stack.append(next_node)
        ans += len(visited)
    print(ans)
