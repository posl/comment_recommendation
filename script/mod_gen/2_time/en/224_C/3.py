def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (X[i] - X[k]) * (Y[j] - Y[k]) - (Y[i] - Y[k]) * (X[j] - X[k]) != 0:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()