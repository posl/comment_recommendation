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
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(C_X - x[i]) + abs(C_Y - y[i])
                    break
            flag = True
            for i in range(n):
                if max(H - abs(C_X - x[i]) - abs(C_Y - y[i]), 0) != h[i]:
                    flag = False
                    break
            if flag:
                print(C_X, C_Y, H)
                return

if __name__ == '__main__':
    main()