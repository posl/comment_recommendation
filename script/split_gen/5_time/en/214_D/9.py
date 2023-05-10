def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x:x[2])
    nodes = [x for x in range(N)]
    def root(x):
        if nodes[x] == x:
            return x
        else:
            nodes[x] = root(nodes[x])
            return nodes[x]
    def unite(x, y):
        nodes[root(x)] = root(y)
    def same(x, y):
        return root(x) == root(y)
    def weight(x, y):
        if same(x, y):
            return 0
        else:
            unite(x, y)
            return edges.pop()[2]
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += weight(i, j)
    print(ans)
