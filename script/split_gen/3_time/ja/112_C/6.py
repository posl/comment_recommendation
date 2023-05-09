def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x_, y_, h_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        h.append(h_)
    for cx in range(101):
        for cy in range(101):
            H = 0
            for i in range(N):
                if h[i] != 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            for i in range(N):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    break
            else:
                print(cx, cy, H)
                return
