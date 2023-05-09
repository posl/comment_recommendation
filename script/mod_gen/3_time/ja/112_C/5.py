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
            H = -1
            for i in range(N):
                if h[i] > 0:
                    tmp = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    if H == -1:
                        H = tmp
                    elif H != tmp:
                        break
            else:
                print(C_X, C_Y, H)
                return

if __name__ == '__main__':
    main()