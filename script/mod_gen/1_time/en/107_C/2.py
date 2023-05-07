def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float("inf")
    for i in range(N - K + 1):
        left = X[i]
        right = X[i + K - 1]
        ans = min(ans, right - left + min(abs(left), abs(right)))
    print(ans)

if __name__ == '__main__':
    main()