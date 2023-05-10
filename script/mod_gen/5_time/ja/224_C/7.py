def get_area(x1, y1, x2, y2, x3, y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            area = get_area(x[i], y[i], x[j], y[j], x[k], y[k])
            if area > 0:
                count += 1
print(count)

if __name__ == '__main__':
    get_area()