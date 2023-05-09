def main():
    N, M, X, T, D = map(int, input().split())
    if N == M:
        print(T)
    elif N == X:
        print(T + (N - M) * D)
    else:
        print(T + (X - M) * D)
