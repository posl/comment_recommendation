def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                if A == 0:
                    A = i + 1
                    B = i + 1
                    C = j + 1
                    D = j + 1
                else:
                    if i + 1 < A:
                        A = i + 1
                    if i + 1 > B:
                        B = i + 1
                    if j + 1 < C:
                        C = j + 1
                    if j + 1 > D:
                        D = j + 1
    print(A, D)
    print(B, C)

if __name__ == '__main__':
    main()