def main():
    # 读取数据
    N = int(input())
    edges = []
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    # 按权重排序
    edges.sort(key=lambda e: e[2])
    # 初始化并查集
    uf = UnionFind(N)
    # 初始化ans
    ans = 0
    # 遍历所有边
    for u, v, w in edges:
        # 计算u和v的连通分量大小
        size = uf.size(u) * uf.size(v)
        # 计算答案
        ans += size * w
        # 连接u和v
        uf.unite(u, v)
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()