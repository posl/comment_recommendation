def judge(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == "W":
                if A[j][i] != "L":
                    return False
            elif A[i][j] == "L":
                if A[j][i] != "W":
                    return
