def main():
    n = int(input())
    x, y, h = [], [], []
    for i in range(n):
        _x, _y, _h = map(int, input().split())
        x.append(_x)
        y.append(_y)
        h.append(_h)
    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            flag = True
            for i in range(n):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    flag = False
                    break
            if flag:
                print(cx, cy, H)
                return

if __name__ == '__main__':
    main()