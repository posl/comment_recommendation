def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(1, X):
        T -= D
    for i in range(X, M):
        T += D
    print(T)
