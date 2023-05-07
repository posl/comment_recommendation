def check_line(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        return x1 == x3
    elif x2 == x3:
        return x1 == x2
    else:
        return (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2)
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if check_line(x1, y1, x2, y2, x3, y3):
                print("Yes")
                exit()
print("No")

if __name__ == '__main__':
    check_line()