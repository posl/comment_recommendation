def main():
    # N = 3
    # D = 2
    # X = [[1, 2], [5, 5], [-2, 8]]
    # N = 3
    # D = 4
    # X = [[-3, 7, 8, 2], [-12, 1, 10, 2], [-2, 8, 9, 3]]
    # N = 5
    # D = 1
    # X = [[1], [2], [3], [4], [5]]
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if (d ** 0.5).is_integer():
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()