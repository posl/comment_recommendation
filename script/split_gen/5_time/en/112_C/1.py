def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    h = [0]*n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                if h[i] > 0:
                    break
            h0 = abs(x[i] - cx) + abs(y[i] - cy) + h[i]
            for i in range(n):
                if h[i] != max(h0 - abs(x[i] - cx) - abs(y[i] - cy), 0):
                    break
            else:
                print(cx, cy, h0)
                exit()
