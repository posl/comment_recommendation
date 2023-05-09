def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    for cx in range(101):
        for cy in range(101):
            Hmax = -1
            for i in range(N):
                if Hmax == -1 and H[i] > 0:
                    Hmax = H[i] + abs(X[i] - cx) + abs(Y[i] - cy)
            if Hmax == -1:
                continue
            flag = True
            for i in range(N):
                if max(Hmax - abs(X[i] - cx) - abs(Y[i] - cy), 0) != H[i]:
                    flag = False
                    break
            if flag:
                print(cx, cy, Hmax)
                return

if __name__ == '__main__':
    main()