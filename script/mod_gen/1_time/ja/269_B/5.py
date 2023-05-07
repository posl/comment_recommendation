def main():
    S = [input() for _ in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i].count("#") != 0:
            A = i + 1
            break
    for i in range(10):
        if S[i].count("#") != 0:
            B = i + 1
    for i in range(10):
        if S[0][i] == "#":
            C = i + 1
            break
    for i in range(10):
        if S[0][i] == "#":
            D = i + 1
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()