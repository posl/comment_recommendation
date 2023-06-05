def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    points.sort(key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                x, y, h = points[i]
                if h != 0:
                    H = h + abs(x - cx) + abs(y - cy)
                    break
            else:
                continue
            for i in range(n):
                x, y, h = points[i]
                if h != max(H - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                print(cx, cy, H)
                return

if __name__ == '__main__':
    main()