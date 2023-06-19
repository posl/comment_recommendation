def bingo_check():
    bingo = False
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2]:
            bingo = True
        if a[0][i] == a[1][i] == a[2][i]:
            bingo = True
    if a[0][0] == a[1][1] == a[2][2]:
        bingo = True
    if a[0][2] == a[1][1] == a[2][0]:
        bingo = True
    return bingo
a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]
for i in range(n):
    for j in range(3):
        for k in range(3):
            if a[j][k] == b[i]:
                a[j][k] = 0
