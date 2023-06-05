def checkbingo(bingo):
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 1:
            return True
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == 1:
            return True
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == 1:
        return True
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == 1:
        return True
    return False
bingo = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    bingo[i] = [int(x) for x in input().split()]
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if bingo[j][k] == b:
                bingo[j][k] = 1
