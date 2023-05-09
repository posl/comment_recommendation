def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        h.append(c)
    for i in range(N):
        if h[i] != 0:
            x1 = x[i]
            y1 = y[i]
            h1 = h[i]
            break
    for C_X in range(101):
        for C_Y in range(101):
            H = h1 + abs(C_X - x1) + abs(C_Y - y1)
            flag = True
            for i in range(N):
                if h[i] != max(H - abs(C_X - x[i]) - abs(C_Y - y[i]), 0):
                    flag = False
                    break
            if flag == True:
                print(C_X, C_Y, H)
                break
        if flag == True:
            break
