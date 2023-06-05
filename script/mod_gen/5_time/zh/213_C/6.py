def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append((a1, i))
        b.append((b1, i))
    a.sort()
    b.sort()
    a1 = 0
    b1 = 0
    a2 = 0
    b2 = 0
    for i in range(n):
        if a[i][0] != a1:
            a2 += 1
        if b[i][0] != b1:
            b2 += 1
        a1 = a[i][0]
        b1 = b[i][0]
        a[i] = (a[i][1], a2)
        b[i] = (b[i][1], b2)
    a.sort()
    b.sort()
    for i in range(n):
        print(a[i][1], b[i][1])
main()
