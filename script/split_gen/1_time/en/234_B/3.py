def main():
    import math
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2))
    print(ans)
