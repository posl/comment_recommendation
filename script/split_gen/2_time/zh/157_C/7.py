def main():
    # 读入数据
    data = []
    for i in range(3):
        data.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    # 生成标记数组
    mark = [[False for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            if data[i][j] in b:
                mark[i][j] = True
    # 判断是否有宾果
    flag = False
    for i in range(3):
        if mark[i][0] and mark[i][1] and mark[i][2]:
            flag = True
            break
        if mark[0][i] and mark[1][i] and mark[2][i]:
            flag = True
            break
    if mark[0][0] and mark[1][1] and mark[2][2]:
        flag = True
    if mark[0][2] and mark[1][1] and mark[2][0]:
        flag = True
    # 输出结果
    if flag:
        print("Yes")
    else:
        print("No")
