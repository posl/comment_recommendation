def main():
    S = [input() for i in range(10)]
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i] == "..........":
            A += 1
        else:
            break
    for i in range(10):
        if S[9-i] == "..........":
            B -= 1
        else:
            break
    for i in range(10):
        if S[0][i] == ".":
            C += 1
        else:
            break
    for i in range(10):
        if S[0][9-i] == ".":
            D -= 1
        else:
            break
    print(A,B)
    print(C,D)

if __name__ == '__main__':
    main()