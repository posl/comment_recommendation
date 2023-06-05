def isConvex(A,B,C,D):
    #计算向量
    AB = (B[0]-A[0],B[1]-A[1])
    BC = (C[0]-B[0],C[1]-B[1])
    CD = (D[0]-C[0],D[1]-C[1])
    DA = (A[0]-D[0],A[1]-D[1])
    #计算向量叉乘
    ABxBC = AB[0]*BC[1]-AB[1]*BC[0]
    BCxCD = BC[0]*CD[1]-BC[1]*CD[0]
    CDxDA = CD[0]*DA[1]-CD[1]*DA[0]
    DAxAB = DA[0]*AB[1]-DA[1]*AB[0]
    #判断正负
    if ABxBC*BCxCD>0 and BCxCD*CDxDA>0 and CDxDA*DAxAB>0:
        return True
    else:
        return False
