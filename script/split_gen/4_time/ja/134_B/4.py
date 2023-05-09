def main():
    N, D = map(int, input().split())
    print(N // (2 * D + 1) + min(1, N % (2 * D + 1)))
