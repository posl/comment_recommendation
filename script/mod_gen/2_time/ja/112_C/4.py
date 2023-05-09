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
            for H in range(1, 1001):
                if h[0] == max(H - abs(x[0] - C_X) - abs(y[0] - C_Y), 0):
                    #print(C_X, C_Y, H)
                    for i in range(N):
                        if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                            break
                        if i == N - 1:
                            print(C_X, C_Y, H)
                            return

if __name__ == '__main__':
    main()