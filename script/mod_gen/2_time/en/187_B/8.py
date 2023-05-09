def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    slopes = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0]:
                slopes[i] += 1
                slopes[j] += 1
            else:
                slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                if -1 <= slope <= 1:
                    slopes[i] += 1
                    slopes[j] += 1
    print(sum([s * (s-1) // 2 for s in slopes]))

if __name__ == '__main__':
    main()