def f(n, k, t, d):
    # 1. 按照t, d排序
    td = [(t[i], d[i]) for i in range(n)]
    td.sort(key=lambda x: (x[0], -x[1]))
    # 2. 按照t, d分组
    td_group = []
    td_group.append([td[0]])
    for i in range(1, n):
        if td[i][0] == td[i - 1][0]:
            td_group[-1].append(td[i])
        else:
            td_group.append([td[i]])
    # 3. 每组取前k个
    td_group = [sorted(x, key=lambda x: -x[1])[:k] for x in td_group]
    # 4. 取最大的k个
    td_group = sorted(td_group, key=lambda x: -sum([y[1] for y in x]))
    td_group = td_group[:k]
    # 5. 计算满意度
    return sum([y[1] for x in td_group for y in x]) + sum([len(x) ** 2 for x in td_group])
n, k = map(int, input().split())
t = []
d = []
for i in range(n):
    t_i, d_i = map(int, input().split())
    t.append(t_i)
    d.append(d_i)
print(f(n, k, t, d))
