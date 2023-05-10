def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
            if slope >= -1 and slope <= 1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()