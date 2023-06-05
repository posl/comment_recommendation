def solve():
    # 读取输入
    n, m, x, t, d = map(int, input().split())
    # 计算
    h = t
    for i in range(x, m):
        h += d
    for i in range(m, n):
        h += d
    # 输出
    print(h)
solve()
