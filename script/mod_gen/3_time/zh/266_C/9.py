def isConvex(A,B,C,D):
    if ((B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0]))*((C[0]-B[0])*(D[1]-C[1])-(C[1]-B[1])*(D[0]-C[0]))<0:
        return False
    if ((C[0]-B[0])*(D[1]-C[1])-(C[1]-B[1])*(D[0]-C[0]))*((D[0]-C[0])*(A[1]-D[1])-(D[1]-C[1])*(A[0]-D[0]))<0:
        return False
    if ((D[0]-C[0])*(A[1]-D[1])-(D[1]-C[1])*(A[0]-D[0]))*((A[0]-D[0])*(B[1]-A[1])-(A[1]-D[1])*(B[0]-A[0]))<0:
        return False
    if ((A[0]-D[0])*(B[1]-A[1])-(A[1]-D[1])*(B[0]-A[0]))*((B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0]))<0:
        return False
    return True

if __name__ == '__main__':
    isConvex()