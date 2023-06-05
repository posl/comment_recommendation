def bingo():
    # 读取输入
    a = []
    for i in range(3):
        a.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    # 判断是否有BINGO
    for i in range(3):
        if a[i][0] in b and a[i][1] in b and a[i][2] in b:
            return "Yes"
    for i in range(3):
        if a[0][i] in b and a[1][i] in b and a[2][i] in b:
            return "Yes"
    if a[0][0] in b and a[1][1] in b and a[2][2] in b:
        return "Yes"
    if a[0][2] in b and a[1][1] in b and a[2][0] in b:
        return "Yes"
    return "No"
