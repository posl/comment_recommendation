def main():
    n = int(input())
    x = [0 for i in range(n)]
    y = [0 for i in range(n)]
    h = [0 for i in range(n)]
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            if h[0] != 0:
                H = h[0] + abs(x[0] - cx) + abs(y[0] - cy)
                break
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                    break
            else:
                print(cx, cy, H)
                exit()
