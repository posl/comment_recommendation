def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    for cx in range(101):
        for cy in range(101):
            h = 0
            for x, y, h0 in points:
                if h0 > 0:
                    h = h0 + abs(cx - x) + abs(cy - y)
                    break
            for x, y, h0 in points:
                if h - abs(cx - x) - abs(cy - y) != h0:
                    break
            else:
                print(cx, cy, h)
                return

if __name__ == '__main__':
    main()