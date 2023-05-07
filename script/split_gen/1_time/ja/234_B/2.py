def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans = max(ans, (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
    print(ans ** 0.5)
