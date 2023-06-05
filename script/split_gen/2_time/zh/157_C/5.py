def solve():
    bingo = [[False for i in range(3)] for j in range(3)]
    for i in range(3):
        bingo[i][0], bingo[i][1], bingo[i][2] = map(int, input().split())
    N = int(input())
    for i in range(N):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if bingo[j][k] == b:
                    bingo[j][k] = True
    flag = False
    for i in range(3):
        if bingo[i][0] and bingo[i][1] and bingo[i][2]:
            flag = True
    for i in range(3):
        if bingo[0][i] and bingo[1][i] and bingo[2][i]:
            flag = True
    if bingo[0][0] and bingo[1][1] and bingo[2][2]:
        flag = True
    if bingo[0][2] and bingo[1][1] and bingo[2][0]:
        flag = True
    if flag:
        print("Yes")
    else:
        print("No")
solve()
