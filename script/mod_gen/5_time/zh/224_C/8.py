def get_area(x1, y1, x2, y2, x3, y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))
n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i:
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]
                if get_area(x1, y1, x2, y2, x3, y3) != 0:
                    cnt += 1
print(cnt//6)

if __name__ == '__main__':
    get_area()