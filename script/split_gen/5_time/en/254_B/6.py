def problem254_b():
    N = int(input())
    A = [[1 for j in range(i+1)] for i in range(N)]
    for i in range(2,N):
        for j in range(1,i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(' '.join(map(str,A[i])))
