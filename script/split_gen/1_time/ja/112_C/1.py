def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for i in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    for cx in range(101):
        for cy in range(101):
            Hmax = 0
            for i in range(N):
                if H[i] != 0:
                    Hmax = H[i] + abs(cx - X[i]) + abs(cy - Y[i])
                    break
            for i in range(N):
                if H[i] != max(Hmax - abs(cx - X[i]) - abs(cy - Y[i]), 0):
                    break
            else:
                print(cx, cy, Hmax)
                return
