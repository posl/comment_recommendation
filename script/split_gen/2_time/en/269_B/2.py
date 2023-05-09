def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i] == ".........":
            continue
        else:
            A = i + 1
            break
    for i in range(10):
        if S[9 - i] == ".........":
            continue
        else:
            B = 10 - i
            break
    for i in range(10):
        if S[0][i] == ".":
            continue
        else:
            C = i + 1
            break
    for i in range(10):
        if S[0][9 - i] == ".":
            continue
        else:
            D = 10 - i
            break
    print(A, B)
    print(C, D)
