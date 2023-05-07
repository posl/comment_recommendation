def main():
    S = [input() for _ in range(10)]
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i].count('#') > 0:
            A = i + 1
            break
    for i in range(10):
        if S[9 - i].count('#') > 0:
            B = 10 - i
            break
    for i in range(10):
        if S[0][i] == '#':
            C = i + 1
            break
    for i in range(10):
        if S[0][9 - i] == '#':
            D = 10 - i
            break
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()