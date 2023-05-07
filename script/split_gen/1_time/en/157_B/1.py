def main():
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    B = []
    for i in range(N):
        B.append(int(input()))
    bingo = False
    for i in range(3):
        if A[i][0] in B and A[i][1] in B and A[i][2] in B:
            bingo = True
            break
    for i in range(3):
        if A[0][i] in B and A[1][i] in B and A[2][i] in B:
            bingo = True
            break
    if A[0][0] in B and A[1][1] in B and A[2][2] in B:
        bingo = True
    if A[0][2] in B and A[1][1] in B and A[2][0] in B:
        bingo = True
    if bingo:
        print("Yes")
    else:
        print("No")
