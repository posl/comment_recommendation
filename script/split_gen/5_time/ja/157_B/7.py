def main():
    a = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    b = [int(input()) for _ in range(n)]
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                a[i][j] = 0
    for i in range(3):
        if a[i].count(0) == 3:
            print('Yes')
            exit()
    for i in range(3):
        if a[0][i] == 0 and a[1][i] == 0 and a[2][i] == 0:
            print('Yes')
            exit()
    if a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
        print('Yes')
        exit()
    if a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
        print('Yes')
        exit()
    print('No')
