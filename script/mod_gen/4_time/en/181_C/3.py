def check_line(a, b, c):
    if (a[0] == b[0] and b[0] == c[0]) or (a[1] == b[1] and b[1] == c[1]):
        return True
    elif (a[0] - b[0]) == 0 or (b[0] - c[0]) == 0:
        return False
    elif (a[1] - b[1]) / (a[0] - b[0]) == (b[1] - c[1]) / (b[0] - c[0]):
        return True
    else:
        return False
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check_line(points[i], points[j], points[k]):
                print("Yes")
                exit()
print("No")

if __name__ == '__main__':
    check_line()