def bingo_check(a):
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2]:
            return True
        elif a[0][i] == a[1][i] == a[2][i]:
            return True
        elif (a[0][0] == a[1][1] == a[2][2]) or (a[0][2] == a[1][1] == a[2][0]):
            return True
    return False
a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = 0
print('Yes' if bingo_check(a) else 'No')
