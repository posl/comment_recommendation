def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y, h = map(int, input().split())
        points.append((x, y, h))
    points = sorted(points, key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            h = points[0][2] + abs(points[0][0] - cx) + abs(points[0][1] - cy)
            for x, y, h0 in points[1:]:
                if h0 != max(h - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                print(cx, cy, h)
                return
