def check(a, b, c):
    if a[0] == b[0] == c[0]:
        return True
    if a[1] == b[1] == c[1]:
        return True
    if a[0] == b[0] or a[0] == c[0] or b[0] == c[0]:
        return False
    if a[1] == b[1] or a[1] == c[1] or b[1] == c[1]:
        return False
    if (a[0] - b[0]) * (a[1] - c[1]) == (a[0] - c[0]) * (a[1] - b[1]):
        return True
    return False
n = int(input())
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
ans = False
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check(xy[i], xy[j], xy[k]):
                ans = True
print("Yes" if ans else "No")

if __name__ == '__main__':
    check()