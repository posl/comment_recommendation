def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = [A[i]+B[i] for i in range(N)]
    D = [i+1 for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    D.sort(reverse=True)
    a = 0
    b = 0
    c = 0
    d = 0
    while a < X:
        print(D[A.index(A[a])])
        A[a] = -1
        a += 1
    while b < Y:
        print(D[B.index(B[b])])
        B[b] = -1
        b += 1
    while c < Z:
        print(D[C.index(C[c])])
        C[c] = -1
        c += 1
    while d < N:
        if A[d] != -1:
            print(D[A.index(A[d])])
            A[d] = -1
        d += 1

if __name__ == '__main__':
    main()