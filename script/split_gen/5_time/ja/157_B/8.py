def checkbingo(bingo):
    #縦横
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == "o":
            return True
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == "o":
            return True
    #斜め
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == "o":
        return True
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == "o":
        return True
    return False
bingo = [[0 for i in range(3)] for j in range(3)]
bingo[1][1] = "o"
for i in range(3):
    bingo[i] = input().split()
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if bingo[j][k] == str(b):
                bingo[j][k] = "o"
