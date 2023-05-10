def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    result = 0
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
    result = A + B + C + D + E
    print(result)
