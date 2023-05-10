def is_cycle(graph, start):
    seen = set()
    to_visit = [start]
    while to_visit:
        node = to_visit.pop()
        if node in seen:
            return True
        seen.add(node)
        to_visit.extend(graph[node])
    return False
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
for i in range(n):
    if is_cycle(graph, i):
        print(-1)
        break
else:
    print(*sorted(range(1, n + 1), key=lambda x: graph[x - 1]))

if __name__ == '__main__':
    is_cycle()