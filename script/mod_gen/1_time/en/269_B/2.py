def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i].find('#') != -1:
            A = i + 1
            break
    for i in range(10):
        if S[9-i].find('#') != -1:
            B = 10 - i
            break
    for i in range(10):
        if S[0][i] == '#':
            C = i + 1
            break
    for i in range(10):
        if S[0][9-i] == '#':
            D = 10 - i
            break
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()