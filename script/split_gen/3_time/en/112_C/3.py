def main():
    N = int(input())
    x = [0]*N
    y = [0]*N
    h = [0]*N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(cx - x[i]) + abs(cy - y[i])
                    break
            if H == -1:
                continue
            for i in range(N):
                if h[i] != max(H - abs(cx - x[i]) - abs(cy - y[i]), 0):
                    break
            else:
                print(cx, cy, H)
                return
