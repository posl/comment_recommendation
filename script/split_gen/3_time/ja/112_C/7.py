def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        X, Y, H = map(int, input().split())
        x.append(X)
        y.append(Y)
        h.append(H)
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(N):
                if max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0) != h[i]:
                    break
            else:
                print(C_X, C_Y, H)
                exit()
