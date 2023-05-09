def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    points.sort()
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()