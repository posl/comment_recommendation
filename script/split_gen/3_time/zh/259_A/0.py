def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(X, M):
        T += D
    for i in range(M, N):
        T += D
    print(T)
