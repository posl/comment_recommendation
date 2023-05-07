def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        _x, _y, _h = map(int, input().split())
        x.append(_x)
        y.append(_y)
        h.append(_h)
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return
