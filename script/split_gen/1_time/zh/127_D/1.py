def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    c = []
    for i in range(m):
        bi,ci = map(int,input().split())
        b.append(bi)
        c.append(ci)
    b = b[::-1]
    c = c[::-1]
    index = 0
    ans = 0
    for i in range(n):
        if index < m and a[i] < c[index]:
            ans += c[index]
            b[index] -= 1
            if b[index] == 0:
                index += 1
        else:
            ans += a[i]
    print(ans)
