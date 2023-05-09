def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    points.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0]:
                continue
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                count += 1
    print(count)
