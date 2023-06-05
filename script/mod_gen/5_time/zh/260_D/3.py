def solve(n,k,p):
    # 为了能够使用bisect库，需要将牌的顺序倒过来
    p = p[::-1]
    # 用于存储每张牌被吃掉的步数
    ans = [0] * n
    # 用于存储桌子上的牌
    table = []
    # 用于存储桌子上的牌的最大值
    table_max = 0
    for i in range(n):
        # 将牌放在桌子上
        table.append(p[i])
        # 如果桌子上有k张牌，就吃掉
        if len(table) == k:
            # 用来存储被吃掉的牌
            eat = []
            # 从桌子上取出牌
            for j in range(k):
                # 如果牌的值大于等于当前桌子上的最大值，就吃掉
                if table[j] >= table_max:
                    eat.append(table[j])
            # 将被吃掉的牌从桌子上删除
            for e in eat:
                table.remove(e)
            # 更新桌子上的最大值
            if len(table) > 0:
                table_max = max(table)
            else:
                table_max = 0
        # 如果桌子上有牌，就将牌放在桌子上最小的牌上面
        if len(table) > 1:
            table.sort()
        # 计算牌被吃掉的步数
        ans[p[i]-1] = i+1
    # 将牌的顺序倒回去
    ans = ans[::-1]
    # 输出结果
    for a in ans:
        print(a)

if __name__ == '__main__':
    solve()