def battle(A,B,C,D):
    while True:
        C=C-B
        if C<=0:
            return "Yes"
            break
        A=A-D
        if A<=0:
