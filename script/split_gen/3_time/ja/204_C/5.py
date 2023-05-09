def main():
    N, M = map(int, input().split())
    print(N * N - N * M - M * N + M * (M - 1) // 2)
