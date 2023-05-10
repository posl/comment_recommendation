def main():
    N = int(input())
    A = [[1 for i in range(N)] for j in range(N)]
    for i in range(2,N):
        for j in range(1,i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(*A[i])

if __name__ == '__main__':
    main()