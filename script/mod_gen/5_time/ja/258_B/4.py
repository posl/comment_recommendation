def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input())))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if i == 0:
                A[i][j] += A[i][j-1]
            elif j == 0:
                A[i][j] += A[i-1][j]
            else:
                A[i][j] += max(A[i-1][j], A[i][j-1])
    print(A[N-1][N-1])

if __name__ == '__main__':
    main()