def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 18
    for i in range(N - K + 1):
        ans = min(ans, abs(x[i]) + abs(x[i] - x[i + K - 1]), abs(x[i + K - 1]) + abs(x[i] - x[i + K - 1]))
    print(ans)
