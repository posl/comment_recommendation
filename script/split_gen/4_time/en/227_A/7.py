def main():
    N, K, A = map(int, input().split())
    print(int((K - A - 1) / (N - 1)) + 1)