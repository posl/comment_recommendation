def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    slopes = []
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0]:
                slopes.append(10000000000)
            else:
                slopes.append((points[i][1] - points[j][1]) / (points[i][0] - points[j][0]))
    slopes = sorted(slopes)
    print(slopes)
    ans = 0
    for i in range(len(slopes)):
        for j in range(i+1, len(slopes)):
            if slopes[i] < slopes[j] and slopes[j] <= 1:
                ans += 1
    print(ans)
