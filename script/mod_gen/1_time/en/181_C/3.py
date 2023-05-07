def check_line(x1, y1, x2, y2, x3, y3):
    if (x1 == x2 and x1 == x3):
        return True
    if (y1 == y2 and y1 == y3):
        return True
    if ((x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2)):
        return True
    return False
n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
flag = False
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if check_line(s[i][0], s[i][1], s[j][0], s[j][1], s[k][0], s[k][1]):
                flag = True
                break
        if (flag):
            break
    if (flag):
        break

if __name__ == '__main__':
    check_line()