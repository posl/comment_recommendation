def main():
    # input
    S = [input() for _ in range(10)]
    # compute
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i + 1
                if B == 0:
                    B = i + 1
                if C == 0:
                    C = j + 1
                if D == 0:
                    D = j + 1
                if i + 1 < A:
                    A = i + 1
                if B < i + 1:
                    B = i + 1
                if j + 1 < C:
                    C = j + 1
                if D < j + 1:
                    D = j + 1
    # output
    print(A, B)
    print(C, D)
