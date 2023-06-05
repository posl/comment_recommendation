def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    if K == 1:
        print(0)
        return
    ans = 10 ** 8
    for i in range(N - K + 1):
        if x[i] <= 0 <= x[i + K - 1]:
            ans = min(ans, min(abs(x[i]), abs(x[i + K - 1])) * 2 + max(abs(x[i]), abs(x[i + K - 1])))
        else:
            ans = min(ans, max(abs(x[i]), abs(x[i + K - 1])))
    print(ans)

if __name__ == '__main__':
    main()