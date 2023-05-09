def main():
    #N: number of rows
    #K: number of columns
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(A)
    #print(N, K)
    #list of median of heights of squares
    median_list = []
    #find median of heights of squares
    for i in range(0, N - K + 1):
        for j in range(0, N - K + 1):
            #print("i = ", i, "j = ", j)
            #print("A[i][j] = ", A[i][j])
            #print("A[i][j+K-1] = ", A[i][j+K-1])
            #print("A[i+K-1][j] = ", A[i+K-1][j])
            #print("A[i+K-1][j+K-1] = ", A[i+K-1][j+K-1])
            median = A[i][j] + A[i+K-1][j+K-1] - A[i+K-1][j] - A[i][j+K-1]
            #print("median = ", median)
            median_list.append(median)
    #print("median_list = ", median_list)
    print(min(median_list))

if __name__ == '__main__':
    main()