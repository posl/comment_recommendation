def bingo():
    a = []
    for i in range(3):
        a.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                a[i][j] = 0
    if a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
        return True
    if a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
        return True
    for i in range(3):
        if a[i][0] == 0 and a[i][1] == 0 and a[i][2] == 0:
            return True
        if a[0][i] == 0 and a[1][i] == 0 and a[2][i] == 0:
            return True
    return False
print('Yes' if bingo() else 'No')
