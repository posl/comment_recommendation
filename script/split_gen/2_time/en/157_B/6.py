def bingo():
    #Read input
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    B = []
    for i in range(N):
        B.append(int(input()))
    #Mark the bingo sheet
    for i in range(3):
        for j in range(3):
            if A[i][j] in B:
                A[i][j] = 1
            else:
                A[i][j] = 0
    #Check if we have a bingo
    for i in range(3):
        if A[i][0] == 1 and A[i][1] == 1 and A[i][2] == 1:
            print("Yes")
            return
        if A[0][i] == 1 and A[1][i] == 1 and A[2][i] == 1:
            print("Yes")
            return
    if A[0][0] == 1 and A[1][1] == 1 and A[2][2] == 1:
        print("Yes")
        return
    if A[0][2] == 1 and A[1][1] == 1 and A[2][0] == 1:
        print("Yes")
        return
    print("No")
