def problem123_b():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if A % 10 != 0:
        A = (A // 10 + 1) * 10
    if B % 10 != 0:
        B = (B // 10 + 1) * 10
    if C % 10 != 0:
        C = (C // 10 + 1) * 10
    if D % 10 != 0:
        D = (D // 10 + 1) * 10
    if E % 10 != 0:
        E = (E // 10 + 1) * 10
    print(A + B + C + D + E)
