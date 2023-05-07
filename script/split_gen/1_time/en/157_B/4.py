def bingo():
    a = []
    for i in range(3):
        a.append(list(map(int,input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                a[i][j] = 0
    if a[0][0] == 0 and a[0][1] == 0 and a[0][2] == 0:
        return 'Yes'
    elif a[1][0] == 0 and a[1][1] == 0 and a[1][2] == 0:
        return 'Yes'
    elif a[2][0] == 0 and a[2][1] == 0 and a[2][2] == 0:
        return 'Yes'
    elif a[0][0] == 0 and a[1][0] == 0 and a[2][0] == 0:
        return 'Yes'
    elif a[0][1] == 0 and a[1][1] == 0 and a[2][1] == 0:
        return 'Yes'
    elif a[0][2] == 0 and a[1][2] == 0 and a[2][2] == 0:
        return 'Yes'
    elif a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
        return 'Yes'
    elif a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
        return 'Yes'
    else:
        return 'No'
print(bingo())
