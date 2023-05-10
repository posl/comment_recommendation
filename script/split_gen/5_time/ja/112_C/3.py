def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x_, y_, h_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        h.append(h_)
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i]-C_X) + abs(y[i]-C_Y)
                    break
            flag = True
            for i in range(n):
                if max(H-abs(x[i]-C_X)-abs(y[i]-C_Y), 0) != h[i]:
                    flag = False
                    break
            if flag:
                print(C_X, C_Y, H)
                exit()
