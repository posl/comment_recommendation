def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 10
    B = 1
    C = 10
    D = 1
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A = min(A, i+1)
                B = max(B, i+1)
                C = min(C, j+1)
                D = max(D, j+1)
    print(A, B)
    print(C, D)
main()
