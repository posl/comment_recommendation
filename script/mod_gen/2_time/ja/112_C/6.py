def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x1, y1, h1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
        h.append(h1)
    for cx in range(101):
        for cy in range(101):
            for i in range(N):
                if h[i] != 0:
                    H = h[i] + abs(cx - x[i]) + abs(cy - y[i])
                    break
            for i in range(N):
                if h[i] != max(H - abs(cx - x[i]) - abs(cy - y[i]), 0):
                    break
            else:
                print(cx, cy, H)
                return

if __name__ == '__main__':
    main()