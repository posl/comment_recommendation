def main():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    for cx in range(101):
        for cy in range(101):
            h = -1
            for x, y, h0 in data:
                if h0 > 0:
                    h = h0 + abs(x - cx) + abs(y - cy)
                    break
            if h < 0:
                continue
            for x, y, h0 in data:
                if h - abs(x - cx) - abs(y - cy) != h0:
                    break
            else:
                print(cx, cy, h)
                return

if __name__ == '__main__':
    main()