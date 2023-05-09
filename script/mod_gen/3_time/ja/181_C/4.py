def calc(x1, y1, x2, y2, x3, y3):
    if x1 == x2 == x3:
        return True
    elif y1 == y2 == y3:
        return True
    elif (x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2):
        return True
    else:
        return False
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if calc(x1, y1, x2, y2, x3, y3):
                print("Yes")
                exit()
print("No")

if __name__ == '__main__':
    calc()