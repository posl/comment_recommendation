def check_on_line(x1, y1, x2, y2, x3, y3):
    return (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1)
N = int(input())
points = []
for i in range(N):
    x,y = map(int, input().split())
    points.append((x,y))
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check_on_line(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()
print('No')

if __name__ == '__main__':
    check_on_line()