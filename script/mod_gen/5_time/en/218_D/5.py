def solve():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points = sorted(points)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in points and (x2, y1) in points:
                ans += 1
    print(ans//2)

if __name__ == '__main__':
    solve()