def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append([x, y])
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                ans += 1
    print(ans)
