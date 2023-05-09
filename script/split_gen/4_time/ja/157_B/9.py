def check_bingo():
    bingo = [False for i in range(8)]
    for i in range(3):
        if bingo[i] == False and A[i][0] == A[i][1] == A[i][2] == "○":
            bingo[i] = True
        if bingo[i+3] == False and A[0][i] == A[1][i] == A[2][i] == "○":
            bingo[i+3] = True
    if bingo[6] == False and A[0][0] == A[1][1] == A[2][2] == "○":
        bingo[6] = True
    if bingo[7] == False and A[0][2] == A[1][1] == A[2][0] == "○":
        bingo[7] = True
    return all(bingo)
A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                A[j][k] = "○"
