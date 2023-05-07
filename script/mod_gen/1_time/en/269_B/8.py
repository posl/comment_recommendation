def main():
    S = [input() for _ in range(10)]
    A = []
    B = []
    C = []
    D = []
    for i in range(10):
        if S[i].count('#') == 10:
            A.append(i + 1)
            B.append(i + 1)
        elif S[i].count('#') == 0:
            pass
        else:
            A.append(i + 1)
            B.append(i + 1)
            for j in range(10):
                if S[i][j] == '#':
                    C.append(j + 1)
                    D.append(j + 1)
    print(min(A), max(B))
    print(min(C), max(D))

if __name__ == '__main__':
    main()