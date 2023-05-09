def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points = sorted(points, key=lambda x: x[0])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += len([k for k in range(j + 1, N) if points[i][0] < points[k][0] < points[j][0] and points[i][1] < points[k][1] < points[j][1]])
    print(ans)
