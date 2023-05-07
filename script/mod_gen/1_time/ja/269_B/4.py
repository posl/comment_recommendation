def main():
    S = [input() for _ in range(10)]
    A = [0] * 10
    B = [0] * 10
    C = [0] * 10
    D = [0] * 10
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A[i] = j + 1
                break
        for j in range(10):
            if S[i][9 - j] == '#':
                B[i] = 10 - j
                break
    for j in range(10):
        for i in range(10):
            if S[i][j] == '#':
                C[j] = i + 1
                break
        for i in range(10):
            if S[9 - i][j] == '#':
                D[j] = 10 - i
                break
    print(max(A), min(B))
    print(max(C), min(D))

if __name__ == '__main__':
    main()