def solve():
    # 读取输入
    n, m = map(int, input().split())
    # 初始化并查集
    uf = UnionFind(n)
    # 读取条件
    for _ in range(m):
        a, b = map(int, input().split())
        uf.union(a - 1, b - 1)
    # 判断是否满足条件
    print("Yes" if uf.all_same() else "No")
    return

if __name__ == '__main__':
    solve()