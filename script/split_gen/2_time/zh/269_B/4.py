def main():
    S = []
    for i in range(10):
        S.append(input())
    A = B = C = D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i + 1
                if C == 0:
                    C = j + 1
                B = i + 1
                D = j + 1
    print(A, B)
    print(C, D)
