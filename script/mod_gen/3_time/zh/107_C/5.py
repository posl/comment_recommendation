def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        left = X[i]
        right = X[i + K - 1]
        ans = min(ans, min(abs(left) + abs(left - right), abs(right) + abs(left - right)))
    print(ans)

if __name__ == '__main__':
    main()