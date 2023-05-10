def main():
    # input
    S = [input() for i in range(10)]
    # compute
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i+1
                if C == 0:
                    C = j+1
                B = i+1
                D = j+1
    # output
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()