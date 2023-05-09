def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if points[i][1] - points[j][1] != 0:
                if -1 <= (points[i][0] - points[j][0]) / (points[i][1] - points[j][1]) <= 1:
                    count += 1
    print(count)
