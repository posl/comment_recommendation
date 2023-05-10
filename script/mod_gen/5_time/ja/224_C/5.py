def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                area = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))
                if area > 0:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()