def is_on_line(x1, y1, x2, y2, x3, y3):
    return (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2)
n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_on_line(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()
print('No')

if __name__ == '__main__':
    is_on_line()