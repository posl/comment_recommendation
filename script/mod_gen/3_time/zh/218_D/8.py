def main():
    n = int(raw_input())
    points = []
    for i in range(n):
        x, y = map(int, raw_input().split())
        points.append((x, y))
    points.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in points and (x2, y1) in points:
                ans += 1
    print ans / 2

if __name__ == '__main__':
    main()