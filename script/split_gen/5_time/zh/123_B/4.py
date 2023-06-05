def solution():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if A % 10 == 0:
        pass
    else:
        A = (A // 10 + 1) * 10
    if B % 10 == 0:
        pass
    else:
        B = (B // 10 + 1) * 10
    if C % 10 == 0:
        pass
    else:
        C = (C // 10 + 1) * 10
    if D % 10 == 0:
        pass
    else:
        D = (D // 10 + 1) * 10
    if E % 10 == 0:
        pass
    else:
        E = (E // 10 + 1) * 10
    return A + B + C + D + E
