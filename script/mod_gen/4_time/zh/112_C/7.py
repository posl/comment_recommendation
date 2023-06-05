def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        h.append(c)
    for i in range(101):
        for j in range(101):
            for k in range(n):
                if h[k] != 0:
                    H = abs(x[k] - i) + abs(y[k] - j) + h[k]
                    break
            for k in range(n):
                if h[k] != max(H-abs(x[k]-i)-abs(y[k]-j), 0):
                    break
            else:
                print(i, j, H)
                return

if __name__ == '__main__':
    main()