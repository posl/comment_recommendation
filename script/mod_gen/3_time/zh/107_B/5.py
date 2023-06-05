def main():
    #读入数据
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    #判断每一行是否都是白色方块
    #如果是白色方块，就删除该行
    #如果不是，就保留该行
    #判断每一列是否都是白色方块
    #如果是白色方块，就删除该列
    #如果不是，就保留该列
    #输出最终结果
    for i in range(h):
        if a[i].count('.') == w:
            a[i] = ''
    for j in range(w):
        if [a[i][j] for i in range(h)].count('.') == h:
            for i in range(h):
                a[i] = a[i][:j] + a[i][j + 1:]
    for i in range(h):
        if a[i] != '':
            print(a[i])

if __name__ == '__main__':
    main()