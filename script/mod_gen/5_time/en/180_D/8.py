def training(X, Y, A, B):
    exp = 0
    while X < Y:
        if X * A < X + B:
            X *= A
            exp += 1
        else:
            X += B
            exp += 1
    return exp - 1
X, Y, A, B = map(int, input().split())
print(training(X, Y, A, B))

if __name__ == '__main__':
    training()