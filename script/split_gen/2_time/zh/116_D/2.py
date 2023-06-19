def main():
    # 读入数据
    n, k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(tuple(map(int, input().split())))
    # 按美味程度降序排列
    s.sort(key=lambda x: x[1], reverse=True)
    # 选出美味程度最大的k个，按配料种类升序排列
    s = sorted(s[:k], key=lambda x: x[0])
    # 计算基本总美味
    base = sum(d for _, d in s)
    # 计算种类奖励
    bonus = sum(i * i for i in range(1, len(set(s)) + 1))
    # 输出结果
    print(base + bonus)
