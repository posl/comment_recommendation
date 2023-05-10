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
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
                if i == N - 1:
                    print(C_X, C_Y, H)
                    exit()
