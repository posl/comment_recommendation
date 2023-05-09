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
    for c_x in range(101):
        for c_y in range(101):
            h_0 = h[0] + abs(c_x - x[0]) + abs(c_y - y[0])
            if h_0 < 0:
                continue
            for i in range(1, n):
                if h[i] != max(h_0 - abs(c_x - x[i]) - abs(c_y - y[i]), 0):
                    break
            else:
                print(c_x, c_y, h_0)
                return

if __name__ == '__main__':
    main()