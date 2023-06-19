def getNum(A,B,C,D):
    res = 0
    for i in range(A,B+1):
        if i % C == 0 and i % D == 0:
            res += 1
    return res
