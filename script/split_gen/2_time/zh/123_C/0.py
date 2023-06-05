def problem123_b():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    M = min(A,B,C,D,E)
    if A%M==0:
        A = A
    else:
        A = A + M - A%M
    if B%M==0:
        B = B
    else:
        B = B + M - B%M
    if C%M==0:
        C = C
    else:
        C = C + M - C%M
    if D%M==0:
        D = D
    else:
        D = D + M - D%M
    if E%M==0:
        E = E
    else:
        E = E + M - E%M
    print(A+B+C+D+E)
problem123_b()
