def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    print(A)
    print(B)
    print(C)
    print(D)

if __name__ == '__main__':
    main()