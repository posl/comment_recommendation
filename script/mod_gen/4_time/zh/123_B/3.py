def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if A % 10 == 0:
        a = A
    else:
        a = (A // 10 + 1) * 10
    if B % 10 == 0:
        b = B
    else:
        b = (B // 10 + 1) * 10
    if C % 10 == 0:
        c = C
    else:
        c = (C // 10 + 1) * 10
    if D % 10 == 0:
        d = D
    else:
        d = (D // 10 + 1) * 10
    if E % 10 == 0:
        e = E
    else:
        e = (E // 10 + 1) * 10
    print(a+b+c+d+e)
main()
