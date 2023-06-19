def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    # print(points)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                ans += 1
    print(ans)
