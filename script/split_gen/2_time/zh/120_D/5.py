def main():
    n, m = map(int, input().split())
    bridge = []
    for i in range(m):
        bridge.append(list(map(int, input().split())))
    bridge.sort(key=lambda x: x[1])
    # print(bridge)
    ans = [0 for i in range(m)]
    uf = UnionFind(n)
    for i in range(m):
        ans[i] = uf.size(bridge[i][0] - 1) * uf.size(bridge[i][1] - 1)
        uf.union(bridge[i][0] - 1, bridge[i][1] - 1)
    for i in range(m - 1, 0, -1):
        ans[i - 1] -= ans[i]
    for i in range(m):
        print(ans[i])
