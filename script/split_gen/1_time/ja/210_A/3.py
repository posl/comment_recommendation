def main():
    N, A, X, Y = map(int, input().split())
    print(min(N, A) * X + max(0, N - A) * Y)
