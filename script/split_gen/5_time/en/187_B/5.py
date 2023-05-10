def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(points[i][0] - points[j][0]) <= abs(points[i][1] - points[j][1]):
                ans += 1
    print(ans)
