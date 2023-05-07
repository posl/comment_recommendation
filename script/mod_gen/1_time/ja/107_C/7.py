def main():
    N, K = [int(x) for x in input().split()]
    X = [int(x) for x in input().split()]
    ans = float('inf')
    for i in range(N - K + 1):
        ans = min(ans, X[i + K - 1] - X[i] + min(abs(X[i]), abs(X[i + K - 1])))
    print(ans)

if __name__ == '__main__':
    main()