def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x1, y1, h1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
        h.append(h1)
    for Cx in range(101):
        for Cy in range(101):
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - Cx) + abs(y[i] - Cy)
                    break
            for i in range(n):
                if h[i] != max(H - abs(x[i] - Cx) - abs(y[i] - Cy), 0):
                    break
            else:
                print(Cx, Cy, H)
                return
