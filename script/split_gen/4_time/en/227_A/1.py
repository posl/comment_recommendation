def main():
    N, K, A = map(int, input().split())
    print((K - N) // (N - 1) + 1 if (K - N) % (N - 1) else (K - N) // (N - 1))
