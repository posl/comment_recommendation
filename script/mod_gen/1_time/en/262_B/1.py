def main():
    N, M = map(int, input().split())
    matrix = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        matrix[a-1][b-1] = 1
        matrix[b-1][a-1] = 1
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[k][i] == 1:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()