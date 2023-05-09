def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    for cx in range(101):
        for cy in range(101):
            h = H[0] + abs(cx - X[0]) + abs(cy - Y[0])
            for i in range(1, N):
                if H[i] != max(h - abs(cx - X[i]) - abs(cy - Y[i]), 0):
                    break
            else:
                print(cx, cy, h)
                return
