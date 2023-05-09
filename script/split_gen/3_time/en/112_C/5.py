def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    for cx in range(101):
        for cy in range(101):
            for hi in range(1, 101):
                if h[0] == 0:
                    continue
                if h[0] != hi + abs(cx - x[0]) + abs(cy - y[0]):
                    continue
                for i in range(1, N):
                    if h[i] != max(hi - abs(cx - x[i]) - abs(cy - y[i]), 0):
                        break
                else:
                    print(cx, cy, hi)
                    return
