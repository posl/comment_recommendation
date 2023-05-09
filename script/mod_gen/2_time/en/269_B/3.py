def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if i + 1 < A:
                    A = i + 1
                if i + 1 > B:
                    B = i + 1
                if j + 1 < C:
                    C = j + 1
                if j + 1 > D:
                    D = j + 1
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()