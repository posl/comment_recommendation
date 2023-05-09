def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            dx = X[i] - X[j]
            dy = Y[i] - Y[j]
            ans = max(ans, abs(dx) + abs(dy))
    print(ans + 1)
