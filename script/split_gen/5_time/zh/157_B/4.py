def bingo():
    # 读取数据
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    # 检查是否有宾果
    for i in range(3):
        if bingo[i][0] in b and bingo[i][1] in b and bingo[i][2] in b:
            return 'Yes'
        if bingo[0][i] in b and bingo[1][i] in b and bingo[2][i] in b:
            return 'Yes'
    if bingo[0][0] in b and bingo[1][1] in b and bingo[2][2] in b:
        return 'Yes'
    if bingo[0][2] in b and bingo[1][1] in b and bingo[2][0] in b:
        return 'Yes'
    return 'No'
print(bingo())
