def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    neighbors = [[] for _ in range(n+1)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    colors = [0] * (n+1)
    max_color = 0
    for a, b in edges:
        neighbor_colors = [colors[x] for x in neighbors[a]]
        neighbor_colors += [colors[x] for x in neighbors[b]]
        neighbor_colors = set(neighbor_colors)
        for i in range(1, n+1):
            if i not in neighbor_colors:
                colors[a] = i
                colors[b] = i
                max_color = max(max_color, i)
                break
    print(max_color)
    for a, b in edges:
        print(colors[a])
solve()
