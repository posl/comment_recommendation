def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    rank = [0 for _ in range(n + 1)]
    ans = 0
    for edge in edges:
        u, v, w = edge
        if find(u, parent) != find(v, parent):
            ans += w * (size(u, parent) * size(v, parent))
            unite(u, v, parent, rank)
    print(ans)

if __name__ == '__main__':
    main()