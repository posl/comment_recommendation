def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points = set(points)
    ans = 0
    for x1, y1 in points:
        for x2, y2 in points:
            if x1 < x2 and y1 < y2:
                if (x1, y2) in points and (x2, y1) in points:
                    ans += 1
    print(ans)
