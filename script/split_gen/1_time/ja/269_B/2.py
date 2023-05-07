def main():
    S = []
    for i in range(10):
        S.append(input())
    A = -1
    B = -1
    C = -1
    D = -1
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                if A == -1:
                    A = i + 1
                if C == -1:
                    C = j + 1
                if A != -1 and B == -1:
                    B = i + 1
                if C != -1 and D == -1:
                    D = j + 1
    print(A,B)
    print(C,D)
