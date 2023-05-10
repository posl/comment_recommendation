def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    max_length = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            length = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            if length > max_length:
                max_length = length
    print(max_length)
