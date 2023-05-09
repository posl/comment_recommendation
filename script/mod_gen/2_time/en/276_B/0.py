def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    d = [0] * N
    for i in range(M):
        d[A[i] - 1] += 1
        d[B[i] - 1] += 1
    #print(d)
    a = [[0] * 0 for i in range(N)]
    for i in range(M):
        a[A[i] - 1].append(B[i])
        a[B[i] - 1].append(A[i])
    #print(a)
    for i in range(N):
        a[i].sort()
        print(d[i], end = " ")
        for j in range(d[i]):
            print(a[i][j], end = " ")
        print()

if __name__ == '__main__':
    main()