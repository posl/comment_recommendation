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
    for cx in range(101):
        for cy in range(101):
            for k in range(n):
                if h[k] > 0:
                    break
            H = h[k] + abs(x[k] - cx) + abs(y[k] - cy)
            flag = True
            for k in range(n):
                if h[k] != max(H - abs(x[k] - cx) - abs(y[k] - cy), 0):
                    flag = False
                    break
            if flag:
                print(cx, cy, H)
                return
