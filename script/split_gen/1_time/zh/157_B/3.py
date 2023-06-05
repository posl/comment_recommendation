def bingo():
    bingo = False
    for i in range(3):
        if a[i][0] in b and a[i][1] in b and a[i][2] in b:
            bingo = True
            break
    for i in range(3):
        if a[0][i] in b and a[1][i] in b and a[2][i] in b:
            bingo = True
            break
    if a[0][0] in b and a[1][1] in b and a[2][2] in b:
        bingo = True
    if a[0][2] in b and a[1][1] in b and a[2][0] in b:
        bingo = True
    if bingo:
        print("Yes")
    else:
        print("No")
a = []
for i in range(3):
    a.append(list(map(int, input().split())))
n = int(input())
b = []
for i in range(n):
    b.append(int(input()))
bingo()
