def solve(n, k, p):
    # 桌子上的牌
    table = []
    # 从上面抽出的牌
    card = []
    # 每张牌被吃掉的步数
    ans = [-1] * n
    # 初始化桌子
    for i in range(n):
        table.append(i + 1)
    # 初始化抽出的牌
    for i in range(n):
        card.append(p[i])
    # 从上面抽出的牌的位置
    pos = 0
    # 抽牌
    for i in range(n):
        # 抽出的牌
        c = card[i]
        # 抽出的牌的位置
        pos = c - 1
        # 抽出的牌的上面的牌
        top = table[pos]
        # 如果桌面上没有牌或者桌面上的牌比抽出的牌大，就把抽出的牌放在桌面上
        if len(table) == 0 or top > c:
            table.append(c)
        # 否则，就把抽出的牌放在桌面上最上面的那张牌上
        else:
            table[top - 1] = c
        # 把桌面上的牌按照从小到大排序
        table.sort()
        # 如果桌面上有k张牌，就把桌面上的牌吃掉
        if len(table) >= k:
            for j in range(k):
                # 把桌面上最小的k张牌吃掉
                ans[table[j] - 1] = i + 1
            # 把桌面上最小的k张牌从桌面上去掉
            table = table[k:]
    # 输出
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    solve()