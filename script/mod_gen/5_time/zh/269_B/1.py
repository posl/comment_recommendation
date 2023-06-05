def main():
    s = []
    for i in range(10):
        s.append(input())
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if A == 0:
                    A = i + 1
                if B < i + 1:
                    B = i + 1
                if C == 0:
                    C = j + 1
                if D < j + 1:
                    D = j + 1
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()