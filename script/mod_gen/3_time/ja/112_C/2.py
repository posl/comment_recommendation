def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    h = [0]*n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(n):
                if h[i] != 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            for i in range(n):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    break
            else:
                print(cx, cy, H)
                return

if __name__ == '__main__':
    main()