def get_area(x1, y1, x2, y2, x3, y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if get_area(x1, y1, x2, y2, x3, y3) != 0:
                count += 1
print(count)

if __name__ == '__main__':
    get_area()