def f(A,B,C,D):
    while True:
        C -= B
        if C <= 0:
            return True
        A -= D
        if A <= 0:
            return False
