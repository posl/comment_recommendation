def main():
    n = int(raw_input())
    points = []
    for i in range(n):
        points.append(map(int, raw_input().split()))
    points.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                continue
            if [points[i][0], points[j][1]] in points and [points[j][0], points[i][1]] in points:
                count += 1
    print count / 2
