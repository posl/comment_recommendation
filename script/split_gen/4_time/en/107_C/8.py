def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    min_time = 10 ** 9
    for i in range(N - K + 1):
        right = X[i + K - 1]
        if X[i] < 0 and right < 0:
            time = -X[i]
        elif X[i] > 0 and right > 0:
            time = right
        else:
            time = min(abs(X[i]), abs(right)) * 2 + max(abs(X[i]), abs(right))
        min_time = min(min_time, time)
    print(min_time)
main()
