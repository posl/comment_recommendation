def is_convex(A,B,C,D):
    #AB X BC
    AB = [B[0]-A[0],B[1]-A[1]]
    BC = [C[0]-B[0],C[1]-B[1]]
    ABxBC = AB[0] * BC[1] - AB[1] * BC[0]
    #BC X CD
    CD = [D[0]-C[0],D[1]-C[1]]
    BCxCD = BC[0] * CD[1] - BC[1] * CD[0]
    #CD X DA
    DA = [A[0]-D[0],A[1]-D[1]]
    CDxDA = CD[0] * DA[1] - CD[1] * DA[0]
    #DA X AB
    DAxAB = DA[0] * AB[1] - DA[1] * AB[0]
    if ABxBC > 0 and BCxCD > 0 and CDxDA > 0 and DAxAB > 0:
        return True
    elif ABxBC < 0 and BCxCD < 0 and CDxDA < 0 and DAxAB < 0:
        return True
    else:
        return False
