def main():
    N, K = map(int, input().split())
    print(sum([100 * n + k for n in range(1, N + 1) for k in range(1, K + 1)]))
