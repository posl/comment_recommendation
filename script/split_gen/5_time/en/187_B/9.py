def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append([int(x) for x in input().split()])
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                result += 1
    print(result)
