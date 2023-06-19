def solve():
    N,M = map(int,input().split())
    B = [list(map(int,input().split())) for i in range(N)]
    #print(N,M,B)
    A = [[0 for i in range(7)] for j in range(N)]
    for i in range(N):
        for j in range(7):
            A[i][j] = (i)*7+j+1
    #print(A)
    for i in range(N):
        for j in range(7):
            if A[i][j] == B[0][0]:
                for k in range(N-i):
                    for l in range(7-j):
                        if A[i+k][j+l] == B[k][l]:
                            pass
                        else:
                            return False
                return True
    return False
