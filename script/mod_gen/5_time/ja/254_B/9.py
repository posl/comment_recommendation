def main():
    N = int(input())
    A = [[0] * N for _ in range(N)]
    A[0][0] = 1
    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        for j in range(i+1):
            if j == 0:
                print(A[i][j], end="")
            else:
                print(" "+str(A[i][j]), end="")
        print()

if __name__ == '__main__':
    main()