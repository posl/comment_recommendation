def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i] == '..........':
            A = i + 1
            B = i + 1
            break
    for i in range(10):
        if S[i] == '##########':
            B = i + 1
            break
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                C = j + 1
                break
        if C != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                D = j + 1
    print(A,B)
    print(C,D)

if __name__ == '__main__':
    main()