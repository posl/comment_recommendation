def solve():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    # 计算所有点的组合
    # 用字典存储
    # 用点的坐标的和作为key
    # 用点的坐标的差作为value
    comb = {}
    for i in range(N):
        for j in range(i+1, N):
            key = points[i][0] + points[j][0], points[i][1] + points[j][1]
            value = points[i][0] - points[j][0], points[i][1] - points[j][1]
            comb.setdefault(key, []).append(value)
    # 计算所有点的组合的数量
    # 用字典存储
    # 用点的坐标的差作为key
    # 用点的坐标的和作为value
    comb_inv = {}
    for key, values in comb.items():
        for value in values:
            comb_inv.setdefault(value, 0)
            comb_inv[value] += 1
    # 从所有点的组合的数量中计算正面积的三角形的数量
    ans = 0
    for value, count in comb_inv.items():
        if value[0] == 0 or value[1] == 0:
            continue
        if (-value[1], value[0]) in comb_inv:
            ans += count * comb_inv[(-value[1], value[0])]
    ans //= 2
    print(ans)

if __name__ == '__main__':
    solve()