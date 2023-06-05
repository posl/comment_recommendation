def get_area(p1, p2, p3):
    return abs((p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
                - p1[0] * p3[1] - p2[0] * p1[1] - p3[0] * p2[1]) / 2)
n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int, input().split())))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if get_area(points[i], points[j], points[k]) > 0:
                count += 1
print(count)

if __name__ == '__main__':
    get_area()