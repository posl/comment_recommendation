def get_area(a, b, c):
    return abs((a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])) / 2
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
result = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            area = get_area(points[i], points[j], points[k])
            if area > 0:
                result += 1
print(result)

if __name__ == '__main__':
    get_area()