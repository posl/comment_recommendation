def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
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
    print(ans//2)
