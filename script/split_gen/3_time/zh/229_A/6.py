def main():
    # 读入数据
    s1 = input()
    s2 = input()
    # 计算黑色方格的个数
    cnt1 = s1.count('#')
    cnt2 = s2.count('#')
    # 判断是否可以从每个黑色方格到达每个黑色方格
    if cnt1 >= 2 and cnt2 >= 2:
        print('Yes')
    else:
        print('No')
