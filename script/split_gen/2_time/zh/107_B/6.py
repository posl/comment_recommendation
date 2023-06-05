def main():
    # 读入数据
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    # 检查是否有黑色方块
    exist_black = False
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                exist_black = True
    # 压缩网格
    ans = []
    for i in range(h):
        if '#' in a[i]:
            ans.append(a[i].replace('.', ''))
    # 转置
    ans = list(map(list, zip(*ans)))
    # 再次压缩
    ans2 = []
    for i in range(w):
        if '#' in ans[i]:
            ans2.append(ans[i])
    # 转置
    ans2 = list(map(list, zip(*ans2)))
    # 输出结果
    if exist_black:
        print('\n'.join([''.join(ans2[i]) for i in range(len(ans2))]))
    else:
        print('')
