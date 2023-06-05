def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    if K == 1:
        print(0)
        return
    ans = 10 ** 9
    for i in range(N - K + 1):
        if X[i] * X[i + K - 1] < 0:
            ans = min(ans, min(abs(X[i]), abs(X[i + K - 1])) * 2 + max(abs(X[i]), abs(X[i + K - 1])))
        else:
            ans = min(ans, max(abs(X[i]), abs(X[i + K - 1])))
    print(ans)

if __name__ == '__main__':
    main()