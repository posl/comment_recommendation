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
            for h in range(101):
                if h == 0:
                    for i in range(N):
                        if h[i] != 0:
                            break
                    else:
                        print(cx, cy, h)
                        return
                else:
                    for i in range(N):
                        if h[i] != max(h - abs(x[i] - cx) - abs(y[i] - cy), 0):
                            break
                    else:
                        print(cx, cy, h)
                        return
main()
