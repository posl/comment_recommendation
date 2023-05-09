def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    for cx in range(101):
        for cy in range(101):
            for h0 in range(1, 101):
                if h[0] == 0:
                    h0 = 0
                for i in range(n):
                    if h[i] != max(h0 - abs(x[i] - cx) - abs(y[i] - cy), 0):
                        break
                    if i == n - 1:
                        print(cx, cy, h0)
                        return
