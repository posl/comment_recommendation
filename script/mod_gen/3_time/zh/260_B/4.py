def main():
    N, X, Y, Z = input().split()
    N = int(N)
    X = int(X)
    Y = int(Y)
    Z = int(Z)
    A = input().split()
    B = input().split()
    A = [int(A[i]) for i in range(N)]
    B = [int(B[i]) for i in range(N)]
    C = [i for i in range(N)]
    C.sort(key=lambda i: -A[i])
    C = C[:X]
    D = [i for i in range(N) if i not in C]
    D.sort(key=lambda i: -B[i])
    D = D[:Y]
    E = [i for i in range(N) if i not in C and i not in D]
    E.sort(key=lambda i: -(A[i] + B[i]))
    E = E[:Z]
    F = C + D + E
    F.sort()
    for i in F:
        print(i + 1)

if __name__ == '__main__':
    main()