def main():
    S = [input() for _ in range(10)]
    A = B = C = D = 0
    for i in range(10):
        if S[i].count('#') > 0:
            if A == 0:
                A = i + 1
            B = i + 1
    for i in range(10):
        if S[0][i] == '#':
            if C == 0:
                C = i + 1
            D = i + 1
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()