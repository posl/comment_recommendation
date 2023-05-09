def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    max_length = 0
    for i in range(N):
        for j in range(i + 1, N):
            length = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            max_length = max(max_length, length)
    print(max_length)
