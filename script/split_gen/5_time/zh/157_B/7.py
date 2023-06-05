def bingo():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    bingo.append([0,0,0])
    bingo.append([0,0,0])
    bingo.append([0,0,0])
    n = int(input())
    for i in range(n):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if bingo[j][k] == b:
                    bingo[j][k] = 0
    for i in range(3):
        if bingo[i][0] == 0 and bingo[i][1] == 0 and bingo[i][2] == 0:
            return 'Yes'
        if bingo[0][i] == 0 and bingo[1][i] == 0 and bingo[2][i] == 0:
            return 'Yes'
    if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0:
        return 'Yes'
    if bingo[0][2] == 0 and bingo[1][1] == 0 and bingo[2][0] == 0:
        return 'Yes'
    return 'No'
print(bingo())
