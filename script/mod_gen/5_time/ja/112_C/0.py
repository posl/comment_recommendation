def main():
    n = int(input())
    x, y, h = [], [], []
    for i in range(n):
        x_, y_, h_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        h.append(h_)
    for cx in range(101):
        for cy in range(101):
            H = []
            for i in range(n):
                if h[i] > 0:
                    H.append(h[i] + abs(x[i] - cx) + abs(y[i] - cy))
            if len(set(H)) == 1:
                print(cx, cy, H[0])
                exit()

if __name__ == '__main__':
    main()