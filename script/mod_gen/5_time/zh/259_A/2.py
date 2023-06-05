def problem259_a():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(1, M):
        if i < X:
            height += D
        else:
            height += D
    print(height)

if __name__ == '__main__':
    problem259_a()