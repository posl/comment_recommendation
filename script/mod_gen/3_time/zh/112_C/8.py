def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        x.append(tmp[0])
        y.append(tmp[1])
        h.append(tmp[2])
    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            for i in range(N):
                if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                    break
            else:
                print(cx, cy, H)
                exit()

if __name__ == '__main__':
    main()