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
    for C_X in range(101):
        for C_Y in range(101):
            H0 = 0
            for i in range(N):
                if H[i] > 0:
                    H0 = H[i] + abs(X[i] - C_X) + abs(Y[i] - C_Y)
                    break
            for i in range(N):
                if H[i] != max(H0 - abs(X[i] - C_X) - abs(Y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H0)
                return
