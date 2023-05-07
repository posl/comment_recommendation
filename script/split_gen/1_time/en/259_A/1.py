def main():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(X, N):
        height += D
    for i in range(0, X):
        height += D
    print(height)
