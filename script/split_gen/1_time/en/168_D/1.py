def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    prev = [-1] * n
    queue = [0]
    while queue:
        current = queue.pop()
        for neighbor in graph[current]:
            if prev[neighbor] == -1:
                prev[neighbor] = current
                queue.append(neighbor)
    if -1 in prev[1:]:
        print('No')
    else:
        print('Yes')
        for i in prev[1:]:
            print(i+1)
