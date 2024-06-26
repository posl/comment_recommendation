def main():
    N = int(input())
    A = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        for j in range(i+1):
            if j == i:
                print(A[i][j])
            else:
                print(A[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()