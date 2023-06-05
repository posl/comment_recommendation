def main():
    N, M = map(int, input().split())
    result = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = (i - 0) ** 2 + (j - 0) ** 2
    for i in range(N):
        for j in range(N):
            result[i][j] = int(result[i][j] ** (1 / 2))
    for i in range(N):
        for j in range(N):
            if result[i][j] ** 2 == (i - 0) ** 2 + (j - 0) ** 2:
                result[i][j] = 0
            else:
                result[i][j] = -1
    for i in range(N):
        for j in range(N):
            if result[i][j] != -1:
                M1 = result[i][j]
                for k in range(N):
                    for l in range(N):
                        if result[k][l] != -1:
                            M2 = result[k][l]
                            if M1 > M2:
                                result[i][j] = M2
                            else:
                                result[i][j] = M1
    for i in range(N):
        for j in range(N):
            print(result[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()