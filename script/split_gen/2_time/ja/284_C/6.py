def main():
    from collections import defaultdict
    import queue
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if visited[i]:
            continue
        ans += 1
        q = queue.Queue()
        q.put(i)
        visited[i] = True
        while not q.empty():
            now = q.get()
            for next in graph[now]:
                if visited[next]:
                    continue
                q.put(next)
                visited[next] = True
    print(ans)
