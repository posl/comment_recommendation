def main():
    N, K, A = map(int, input().split())
    print((K - A + N - 1) % N + 1)
