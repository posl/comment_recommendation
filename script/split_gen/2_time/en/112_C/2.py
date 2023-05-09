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
    
    for i in range(101):
        for j in range(101):
            H = h[0] + abs(x[0] - i) + abs(y[0] - j)
            for k in range(1, N):
                if h[k] != max(H - abs(x[k] - i) - abs(y[k] - j), 0):
                    break
            else:
                print(i, j, H)
                break
