def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y, h = map(int, input().split())
        points.append((x, y, h))
    for cx in range(101):
        for cy in range(101):
            h = max([p[2] + abs(p[0] - cx) + abs(p[1] - cy) for p in points if p[2] > 0])
            if all([max(h - abs(p[0] - cx) - abs(p[1] - cy), 0) == p[2] for p in points]):
                print(cx, cy, h)
                return
