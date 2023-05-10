def check_bingo():
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2]:
            return True
        if bingo[0][i] == bingo[1][i] == bingo[2][i]:
            return True
    if bingo[0][0] == bingo[1][1] == bingo[2][2]:
        return True
    if bingo[0][2] == bingo[1][1] == bingo[2][0]:
        return True
    return False
bingo = []
for i in range(3):
    bingo.append(list(map(int, input().split())))
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if bingo[j][k] == b:
                bingo[j][k] = 0
                break
