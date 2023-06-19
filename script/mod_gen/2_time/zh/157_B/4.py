def bingo():
    bingo = []
    for i in range(3):
        bingo.append(list(map(int, input().split())))
    N = int(input())
    b = []
    for i in range(N):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            if bingo[i][j] in b:
                bingo[i][j] = 0
    if bingo[0][0] + bingo[1][1] + bingo[2][2] == 0:
        return 'Yes'
    elif bingo[0][2] + bingo[1][1] + bingo[2][0] == 0:
        return 'Yes'
    elif bingo[0][0] + bingo[0][1] + bingo[0][2] == 0:
        return 'Yes'
    elif bingo[1][0] + bingo[1][1] + bingo[1][2] == 0:
        return 'Yes'
    elif bingo[2][0] + bingo[2][1] + bingo[2][2] == 0:
        return 'Yes'
    elif bingo[0][0] + bingo[1][0] + bingo[2][0] == 0:
        return 'Yes'
    elif bingo[0][1] + bingo[1][1] + bingo[2][1] == 0:
        return 'Yes'
    elif bingo[0][2] + bingo[1][2] + bingo[2][2] == 0:
        return 'Yes'
    else:
        return 'No'
print(bingo())
