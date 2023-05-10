def main():
    N, M = map(int, input().split())
    print(N * (N - 1) // 2 - M)
