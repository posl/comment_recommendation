def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(X):
        T += D
    for i in range(N-X):
        T -= D
    print(T)
