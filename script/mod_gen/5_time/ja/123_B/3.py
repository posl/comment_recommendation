def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min = A
    if B < min:
        min = B
    if C < min:
        min = C
    if D < min:
        min = D
    if E < min:
        min = E
    if A % 10 == 0:
        A = A
    else:
        A = (A // 10 + 1) * 10
    if B % 10 == 0:
        B = B
    else:
        B = (B // 10 + 1) * 10
    if C % 10 == 0:
        C = C
    else:
        C = (C // 10 + 1) * 10
    if D % 10 == 0:
        D = D
    else:
        D = (D // 10 + 1) * 10
    if E % 10 == 0:
        E = E
    else:
        E = (E // 10 + 1) * 10
    print(A + B + C + D + E - 10 + min)

if __name__ == '__main__':
    main()