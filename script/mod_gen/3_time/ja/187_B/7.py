def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    points.sort()
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (points[j][1] - points[i][1]) * 2 <= points[j][0] - points[i][0]:
                count += 1
    print(count)
main()

if __name__ == '__main__':
    main()