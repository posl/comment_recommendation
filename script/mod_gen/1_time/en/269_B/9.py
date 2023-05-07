def main():
    # 10 strings
    S = [input() for _ in range(10)]
    #print(S)
    # A, B, C, D
    A, B, C, D = -1, -1, -1, -1
    # A, B
    for i in range(10):
        if S[i][0] == '#':
            A = i + 1
            break
    for i in range(10):
        if S[i][9] == '#':
            B = i + 1
            break
    # C, D
    for j in range(10):
        if S[0][j] == '#':
            C = j + 1
            break
    for j in range(10):
        if S[9][j] == '#':
            D = j + 1
            break
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()