def checkBingo(a):
    #check row
    for i in range(0, 3):
        if a[i][0] == a[i][1] == a[i][2] == True:
            return True
    #check col
    for i in range(0, 3):
        if a[0][i] == a[1][i] == a[2][i] == True:
            return True
    #check diagonal
    if a[0][0] == a[1][1] == a[2][2] == True:
        return True
    if a[0][2] == a[1][1] == a[2][0] == True:
        return True
    return False
a = [[False for i in range(3)] for j in range(3)]
for i in range(0, 3):
    a[i] = [int(x) for x in input().split()]
n = int(input())
b = [int(input()) for i in range(0, n)]
for i in range(0, n):
    for j in range(0, 3):
        for k in range(0, 3):
            if a[j][k] == b[i]:
                a[j][k] = True
