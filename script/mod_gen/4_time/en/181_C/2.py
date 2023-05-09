def check(x1, y1, x2, y2, x3, y3):
    if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
        return True
    return False
n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if check(xy[i][0], xy[i][1], xy[j][0], xy[j][1], xy[k][0], xy[k][1]):
                print("Yes")
                exit()
print("No")

if __name__ == '__main__':
    check()