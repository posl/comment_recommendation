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
        a = 10
    if b == 0:
        b = 10
    if c == 0:
        c = 10
    if d == 0:
        d = 10
    if e == 0:
        e = 10
    if A % 10 == 0:
        A = A - 10
    else:
        A = A - A % 10
    if B % 10 == 0:
        B = B - 10
    else:
        B = B - B % 10
    if C % 10 == 0:
        C = C - 10
    else:
        C = C - C % 10
    if D % 10 == 0:
        D = D - 10
    else:
        D = D - D % 10
    if E % 10 == 0:
        E = E - 10
    else:
        E = E - E % 10
    if a + b + c + d + e == 10:
        print(A + B + C + D + E + 10)
    else:
        print(A + B + C + D + E)
