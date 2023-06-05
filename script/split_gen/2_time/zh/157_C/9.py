def bingo():
    bingo = False
    for i in range(3):
        if A[i][0] in b and A[i][1] in b and A[i][2] in b:
            bingo = True
        if A[0][i] in b and A[1][i] in b and A[2][i] in b:
            bingo = True
    if A[0][0] in b and A[1][1] in b and A[2][2] in b:
        bingo = True
    if A[0][2] in b and A[1][1] in b and A[2][0] in b:
        bingo = True
    return bingo
A = [[0]*3 for i in range(3)]
for i in range(3):
    A[i] = list(map(int, input().split()))
N = int(input())
b = []
for i in range(N):
    b.append(int(input()))
bingo = bingo()
