def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(list(map(int, input().split())))
    B = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        for j in range(A[i][0]):
            for k in range(j+1, A[i][0]):
                B[A[i][j+1]-1][A[i][k+1]-1] = 1
                B[A[i][k+1]-1][A[i][j+1]-1] = 1
    for i in range(N):
        for j in range(N):
            if B[i][j] == 0:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()