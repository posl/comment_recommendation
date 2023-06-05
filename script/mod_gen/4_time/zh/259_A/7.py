def problem259_a():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(X, M):
        height += D
    for i in range(M, N):
        height += D
    print(height)

if __name__ == '__main__':
    problem259_a()