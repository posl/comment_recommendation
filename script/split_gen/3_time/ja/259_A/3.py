def main():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(X, N):
        height += D
    print(height)
