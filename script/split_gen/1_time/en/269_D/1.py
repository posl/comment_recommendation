def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    # 1. (x, y) -> (x, y + x) -> (x - y, 2x + y)
    X2 = [0] * N
    Y2 = [0] * N
    for i in range(N):
        X2[i] = X[i] - Y[i]
        Y2[i] = 2 * X[i] + Y[i]
    # 2. (x, y) -> (x + y, y) -> (2x + y, x - y)
    X3 = [0] * N
    Y3 = [0] * N
    for i in range(N):
        X3[i] = 2 * X[i] + Y[i]
        Y3[i] = X[i] - Y[i]
    # 3. (x, y) -> (x, y - x) -> (x + y, -2x + y)
    X4 = [0] * N
    Y4 = [0] * N
    for i in range(N):
        X4[i] = X[i] + Y[i]
        Y4[i] = -2 * X[i] + Y[i]
    # 4. (x, y) -> (x - y, y) -> (-2x + y, x + y)
    X5 = [0] * N
    Y5 = [0] * N
    for i in range(N):
        X5[i] = -2 * X[i] + Y[i]
        Y5[i] = X[i] + Y[i]
    # 5. (x, y) -> (x, -y) -> (-x, -y)
    X6 = [0] * N
    Y6 = [0] * N
    for i in range(N):
        X6[i] = -X[i]
        Y6[i] = -Y[i]
    # 6. (x, y) -> (-x, y) -> (-x, -y)
    X7 = [0] * N
    Y7 = [0
