def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    a = A
    b = B
    c = C
    d = D
    e = E
    if A % 10 != 0:
        A = A + (10 - (A % 10))
    if B % 10 != 0:
        B = B + (10 - (B % 10))
    if C % 10 != 0:
        C = C + (10 - (C % 10))
    if D % 10 != 0:
        D = D + (10 - (D % 10))
    if E % 10 != 0:
        E = E + (10 - (E % 10))
    print(A + B + C + D + E - 10 - max(A, B, C, D, E))
    return 0

if __name__ == '__main__':
    main()