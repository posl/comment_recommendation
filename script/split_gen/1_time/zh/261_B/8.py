def check(i,j):
    #print("i=",i,"j=",j)
    #print("A[i][j]=",A[i][j])
    #print("A[j][i]=",A[j][i])
    if A[i][j] == "W":
        if A[j][i] != "L":
            return False
    elif A[i][j] ==
