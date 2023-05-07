def bingo():
    a = []
    for i in range(3):
        a.append([int(x) for x in input().split()])
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                a[i][j] = 0
    if a[0][0] == a[0][1] == a[0][2] == 0 or a[1][0] == a[1][1] == a[1][2] == 0 or a[2][0] == a[2][1] == a[2][2] == 0:
        print("Yes")
        return
    if a[0][0] == a[1][1] == a[2][2] == 0 or a[0][2] == a[1][1] == a[2][0] == 0:
        print("Yes")
        return
    if a[0][0] == a[1][0] == a[2][0] == 0 or a[0][1] == a[1][1] == a[2][1] == 0 or a[0][2] == a[1][2] == a[2][2] == 0:
        print("Yes")
        return
    print("No")
bingo()
