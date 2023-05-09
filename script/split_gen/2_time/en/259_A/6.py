def solution():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + D * (N - X))
    else:
        print(T + D * (M - X))
