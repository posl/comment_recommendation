def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    edges.sort(key=lambda x: x[2], reverse=True)
    parents = list(range(n+1))
    sizes = [1] * (n+1)
    def find(x):
        if parents[x] == x:
            return x
        else:
            parents[x] = find(parents[x])
            return parents[x]
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            if sizes[px] < sizes[py]:
                px, py = py, px
            parents[py] = px
            sizes[px] += sizes[py]
    ans = 0
    for u, v, w in edges:
        ans += w * sizes[find(u)] * sizes[find(v)]
        union(u, v)
    print(ans)

if __name__ == '__main__':
    main()