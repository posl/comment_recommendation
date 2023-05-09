def main():
    N, M, X, T, D = map(int, input().split())
    #print(N, M, X, T, D)
    if M < X:
        print(T + D * (N - X))
    else:
        print(T + D * (N - M - 1))
