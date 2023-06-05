def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    # 位置i的牌，被吃掉的时间
    ans = [-1]*n
    # 桌面上的牌
    table = []
    # 桌面上的牌的最小值
    min_table = float('inf')
    for i in range(n):
        # 抽出的牌的值
        x = p[i]
        # 抽出的牌的位置
        x_pos = i+1
        # 如果桌面上有牌
        if table:
            # 如果抽出的牌的值大于桌面上的牌的最小值
            if x > min_table:
                # 将抽出的牌放到桌面上，不叠加在任何牌上
                table.append(x)
            else:
                # 将抽出的牌放到桌面上，叠加在最小值上
                table.append(x)
                # 桌面上的牌的最小值更新
                min_table = x
                # 如果桌面上的牌的数量大于k
                if len(table) > k:
                    # 抽出的牌被吃掉
                    ans[x_pos-1] = i-k+1
                    # 桌面上的牌的最小值更新
                    min_table = min(table[-k:])
        else:
            # 将抽出的牌放到桌面上，不叠加在任何牌上
            table.append(x)
        # 如果桌面上的牌的数量大于k
        if len(table) > k:
            # 抽出的牌被吃掉
            ans[x_pos-1] = i-k+1
            # 桌面上的牌的最小值更新
            min_table = min(table[-k:])
    # 输出答案
    for i in range(n):
        print(ans[i])
