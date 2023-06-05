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
    for C_X in range(101):
        for C_Y in range(101):
            H = h[0] + abs(x[0] - C_X) + abs(y[0] - C_Y)
            if all(h_i == max(H - abs(x_i - C_X) - abs(y_i - C_Y), 0) for x_i, y_i, h_i in zip(x, y, h)):
                print(C_X, C_Y, H)
                return

if __name__ == '__main__':
    main()