def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    points.sort(key=lambda x: x[0])
    result = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            count = 0
            for k in range(N):
                if points[i][0] <= points[k][0] <= points[j][0] and points[i][1] <= points[k][1] <= points[j][1]:
                    count += 1
            result += count * (count - 1) // 2
    print(result)
main()
