def main():
    n, d = map(int, input().split())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = 0
            for k in range(d):
                distance += (points[i][k] - points[j][k])**2
            if (distance**0.5).is_integer():
                count += 1
    print(count)
