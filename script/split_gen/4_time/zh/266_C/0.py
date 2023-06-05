def judgeConvex(A,B,C,D):
    #AB,BC,CD,DA
    if (B[0]-A[0])*(C[1]-B[1])-(C[0]-B[0])*(B[1]-A[1])<0:
        return False
    if (C[0]-B[0])*(D[1]-C[1])-(D[0]-C[0])*(C[1]-B[1])<0:
        return False
    if (D[0]-C[0])*(A[1]-D[1])-(A[0]-D[0])*(D[1]-C[1])<0:
        return False
    if (A[0]-D[0])*(B[1]-A[1])-(B[0]-A[0])*(A[1]-D[1])<0:
        return False
    return True
