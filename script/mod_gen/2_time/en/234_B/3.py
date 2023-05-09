def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    max_dist = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if dist > max_dist:
                max_dist = dist
    print(max_dist)

if __name__ == '__main__':
    main()