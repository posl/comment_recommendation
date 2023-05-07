def main():
    N = int(input())
    x, y, h = [0] * N, [0] * N, [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            flg = True
            for i in range(N):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    flg = False
                    break
            if flg:
                print(cx, cy, H)
                return
