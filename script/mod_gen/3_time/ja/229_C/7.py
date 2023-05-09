def main():
    N, W = map(int, input().split())
    C = []
    for _ in range(N):
        a, b = map(int, input().split())
        C.append((a, b))
    C.sort()
    dp = [0] * (W + 1)
    for a, b in C:
        for w in range(W, b - 1, -1):
            dp[w] = max(dp[w], dp[w - b] + a)
    print(dp[-1])

if __name__ == '__main__':
    main()