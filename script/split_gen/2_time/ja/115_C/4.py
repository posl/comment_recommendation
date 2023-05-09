def main():
    N, K = map(int, input().split())
    hs = [int(input()) for _ in range(N)]
    hs.sort()
    min_diff = 10 ** 9
    for i in range(N - K + 1):
        min_diff = min(min_diff, hs[i + K - 1] - hs[i])
    print(min_diff)
