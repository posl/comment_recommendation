def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            if (x1 - dx, y1 - dy) not in points:
                ans += 1
            if (x2 + dx, y2 + dy) not in points:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()