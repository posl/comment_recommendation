def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    for i in range(1, N+1):
        d = 0
        for j in range(M):
            if i == A[j]:
                d += 1
            elif i == B[j]:
                d += 1
        print(d, end=" ")
        for j in range(M):
            if i == A[j]:
                print(B[j], end=" ")
            elif i == B[j]:
                print(A[j], end=" ")
        print()

if __name__ == '__main__':
    main()