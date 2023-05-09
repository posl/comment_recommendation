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
    for C_X in range(101):
        for C_Y in range(101):
            H = h[0] + abs(x[0] - C_X) + abs(y[0] - C_Y)
            for i in range(1, N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

if __name__ == '__main__':
    main()