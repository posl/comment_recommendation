def problems123_b():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A, B, C, D, E)
    if min_time == A:
        min_time = 0
    elif min_time == B:
        min_time = 10
    elif min_time == C:
        min_time = 20
    elif min_time == D:
        min_time = 30
    else:
        min_time = 40
    if A % 10 == 0:
        A = A
    else:
        A = A + (10 - A % 10)
    if B % 10 == 0:
        B = B
    else:
        B = B + (10 - B % 10)
    if C % 10 == 0:
        C = C
    else:
        C = C + (10 - C % 10)
    if D % 10 == 0:
        D = D
    else:
        D = D + (10 - D % 10)
    if E % 10 == 0:
        E = E
    else:
        E = E + (10 - E % 10)
    print(A + B + C + D + E - 50 + min_time)
