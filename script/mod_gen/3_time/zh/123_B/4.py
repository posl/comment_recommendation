def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    a = A % 10
    b = B % 10
    c = C % 10
    d = D % 10
    e = E % 10
    if a == 0:
        pass
    else:
        A = A + (10 - a)
    if b == 0:
        pass
    else:
        B = B + (10 - b)
    if c == 0:
        pass
    else:
        C = C + (10 - c)
    if d == 0:
        pass
    else:
        D = D + (10 - d)
    if e == 0:
        pass
    else:
        E = E + (10 - e)
    if A == B == C == D == E:
        print(A)
    elif A > B and A > C and A > D and A > E:
        print(A)
    elif B > A and B > C and B > D and B > E:
        print(B)
    elif C > A and C > B and C > D and C > E:
        print(C)
    elif D > A and D > B and D > C and D > E:
        print(D)
    elif E > A and E > B and E > C and E > D:
        print(E)

if __name__ == '__main__':
    main()