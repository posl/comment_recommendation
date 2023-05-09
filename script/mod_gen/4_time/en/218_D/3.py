def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x,y))
    points.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                if (points[i][0], points[j][1]) in points and (points[j][0], points[i][1]) in points:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()