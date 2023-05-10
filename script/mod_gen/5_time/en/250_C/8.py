def swap(x, y):
    global a
    global b
    global c
    if a[x] == 0:
        a[y] += 1
    else:
        a[y] += a[x] + 1
        a[x] = 0
    if a[y] == b:
        c = y
        return
    swap(y, y+1)
n, q = map(int, input().split())
a = [0] * n
b = 0
c = 0
for i in range(q):
    x = int(input()) - 1
    if a[x] == 0:
        a[x] = 1
        if x == b:
            b += 1
        elif x == c:
            c += 1
    else:
        a[x] += 1
    if a[x] == b:
        c = x
    elif a[x] == b + 1:
        c = x + 1
    elif a[x] == b + 2:
        c = x + 2
    else:
        c = x + a[x]
    swap(x, x+1)
for i in range(n):
    print(a[i], end=' ')
print()

if __name__ == '__main__':
    swap()