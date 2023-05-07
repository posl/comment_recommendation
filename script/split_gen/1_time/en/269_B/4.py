def main():
    S = [input() for i in range(10)]
    A, B = 10, 1
    C, D = 10, 1
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A = min(A, i)
                B = max(B, i)
                C = min(C, j)
                D = max(D, j)
    print(A + 1, B + 1)
    print(C + 1, D + 1)
