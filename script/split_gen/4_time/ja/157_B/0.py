def check(bingo):
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
bingo = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]
for i in range(3):
    for j in range(3):
        if bingo[i][j] in b:
            bingo[i][j] = 0
