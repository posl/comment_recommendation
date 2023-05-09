def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for i in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    ans = [0, 0, 0]
    for cx in range(101):
        for cy in range(101):
            for i in range(N):
                if H[i] != 0:
                    h = H[i] + abs(cx - X[i]) + abs(cy - Y[i])
                    break
            else:
                continue
            for i in range(N):
                if max(h - abs(cx - X[i]) - abs(cy - Y[i]), 0) != H[i]:
                    break
            else:
                ans = [cx, cy, h]
                break
        else:
            continue
        break
    print(*ans)
