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
    for cx in range(101):
        for cy in range(101):
            for h in range(101):
                if h == 0:
                    if (cx, cy) in zip(X, Y):
                        continue
                    else:
                        break
                flag = True
                for x, y, hh in zip(X, Y, H):
                    if h != hh + abs(x - cx) + abs(y - cy):
                        flag = False
                        break
                if flag:
                    print(cx, cy, h)
                    return
