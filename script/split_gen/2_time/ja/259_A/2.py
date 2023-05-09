def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        for i in range(M, X):
            T -= D
    elif M > X:
        for i in range(X, M):
            T += D
    print(T)
