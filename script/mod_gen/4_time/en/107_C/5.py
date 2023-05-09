def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    min_time = 10 ** 10
    for i in range(N - K + 1):
        if X[i] < 0 and X[i + K - 1] < 0:
            time = -X[i]
        elif X[i] > 0 and X[i + K - 1] > 0:
            time = X[i + K - 1]
        else:
            time = min(-X[i] * 2 + X[i + K - 1], X[i + K - 1] * 2 - X[i])
        if time < min_time:
            min_time = time
    print(min_time)

if __name__ == '__main__':
    main()