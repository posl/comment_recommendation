def isMatched(A,B,N):
    for i in range(1,100):
        for j in range(1,8):
            if A[i][j]==B[1][1]:
                if i+N-1>100:
                    return False
                for k in range(1,N+1):
                    for l in range(1,8):
                        if A[i+k-1][l]!=B[k][l]:
                            return False
                return True
    return False

if __name__ == '__main__':
    isMatched()