def main():
    N, K = map(int, input().split())
    h = sorted([int(input()) for _ in range(N)])
    min_diff = 10 ** 9
    for i in range(N - K + 1):
        min_diff = min(min_diff, h[i + K - 1] - h[i])
    print(min_diff)
