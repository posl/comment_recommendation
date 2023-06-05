def solve():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    t = 0
    if A % 10 != 0:
        t += (A // 10 + 1) * 10
    else:
        t += A
    if B % 10 != 0:
        t += (B // 10 + 1) * 10
    else:
        t += B
    if C % 10 != 0:
        t += (C // 10 + 1) * 10
    else:
        t += C
    if D % 10 != 0:
        t += (D // 10 + 1) * 10
    else:
        t += D
    if E % 10 != 0:
        t += (E // 10 + 1) * 10
    else:
        t += E
    print(t)

if __name__ == '__main__':
    solve()