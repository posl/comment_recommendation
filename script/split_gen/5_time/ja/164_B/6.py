def judge(A,B,C,D):
    while True:
        C = C - B
        if C <= 0:
            return True
        A = A - D
        if A <= 0:
            return False
