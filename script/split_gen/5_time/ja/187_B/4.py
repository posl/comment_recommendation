def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if -1 <= (points[j][1] - points[i][1])/(points[j][0] - points[i][0]) <= 1:
                ans += 1
    print(ans)
