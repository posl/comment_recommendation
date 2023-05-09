def main():
    N = int(input())
    #N = 3
    #x = [99, 100, 99]
    #y = [1, 1, 0]
    #h = [191, 192, 192]
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
            for H in range(1, max(h)+1):
                if h[0] == H - abs(x[0]-C_X) - abs(y[0]-C_Y):
                    flag = 1
                    for i in range(1, N):
                        if h[i] != max(H - abs(x[i]-C_X) - abs(y[i]-C_Y), 0):
                            flag = 0
                            break
                    if flag == 1:
                        print(C_X, C_Y, H)
                        return 0

if __name__ == '__main__':
    main()