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
    for c_x in range(101):
        for c_y in range(101):
            h = 0
            for i in range(N):
                if H[i] > 0:
                    h = H[i] + abs(c_x - X[i]) + abs(c_y - Y[i])
                    break
            for i in range(N):
                if H[i] != max(h - abs(c_x - X[i]) - abs(c_y - Y[i]), 0):
                    break
            else:
                print(c_x, c_y, h)
                return
