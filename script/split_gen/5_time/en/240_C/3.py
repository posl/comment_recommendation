def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    s = 0
    for i in range(n):
        if i%2 == 0:
            s += b[i]
        else:
            s += a[i]
    if s >= x:
        print("Yes")
    else:
        print("No")
