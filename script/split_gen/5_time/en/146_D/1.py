def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    graph = [[] for _ in range(n)]
    for a, b in ab:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    color = [0] * n
    color[0] = 1
    color[1] = 2
    color[2] = 3
    queue = [0]
    while queue:
        v = queue.pop()
        c = color[v]
        for u in graph[v]:
            if color[u] == 0:
                c += 1
                if c > 3:
                    c = 1
                color[u] = c
                queue.append(u)
    print(max(color))
    for i in range(n-1):
        print(color[ab[i][0]-1])
