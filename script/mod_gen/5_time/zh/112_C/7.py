def main():
    N = int(input())
    x, y, h = [], [], []
    for i in range(N):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        h.append(c)
    for Cx in range(101):
        for Cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    tmp = h[i] + abs(x[i] - Cx) + abs(y[i] - Cy)
                    if H == -1:
                        H = tmp
                    elif H != tmp:
                        break
            else:
                print(Cx, Cy, H)
                return

if __name__ == '__main__':
    main()