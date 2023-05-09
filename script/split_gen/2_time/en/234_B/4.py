def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            length = ((x1-x2)**2 + (y1-y2)**2)**0.5
            max_length = max(max_length, length)
    print(max_length)
