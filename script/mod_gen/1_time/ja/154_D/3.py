def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    P = [0] * (N + 1)
    for i in range(N):
        P[i + 1] = P[i] + p[i]
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, (P[i + K] - P[i]) / 2 + P[i])
    print(ans)

if __name__ == '__main__':
    main()