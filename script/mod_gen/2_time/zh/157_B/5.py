def bingo():
    bingo = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        bingo[i] = list(map(int,input().split()))
    N = int(input())
    b = [0 for i in range(N)]
    for i in range(N):
        b[i] = int(input())
    #print(bingo)
    #print(b)
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if b[i] == bingo[j][k]:
                    bingo[j][k] = 0
    #print(bingo)
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == 0:
            return "Yes"
        elif bingo[0][i] == bingo[1][i] == bingo[2][i] == 0:
            return "Yes"
        elif bingo[0][0] == bingo[1][1] == bingo[2][2] == 0:
            return "Yes"
        elif bingo[0][2] == bingo[1][1] == bingo[2][0] == 0:
            return "Yes"
    return "No"
print(bingo())
