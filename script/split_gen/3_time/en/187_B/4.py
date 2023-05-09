def solve():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if -1 <= (y2 - y1) / (x2 - x1) <= 1:
                count += 1
    print(count)
