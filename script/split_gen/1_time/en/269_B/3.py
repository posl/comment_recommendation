def main():
    S = [input() for _ in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                A = i + 1
                break
        if A != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[9 - i][j] == "#":
                B = 10 - i
                break
        if B != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[j][i] == "#":
                C = i + 1
                break
        if C != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[j][9 - i] == "#":
                D = 10 - i
                break
        if D != 0:
            break
    print(A, B)
    print(C, D)
