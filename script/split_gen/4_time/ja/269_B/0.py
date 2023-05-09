def main():
    S = [input() for i in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i + 1
                if B < i + 1:
                    B = i + 1
                if C == 0:
                    C = j + 1
                if D < j + 1:
                    D = j + 1
    print(A, B)
    print(C, D)
