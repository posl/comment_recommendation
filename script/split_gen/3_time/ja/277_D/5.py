def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0] * m
    for i in a:
        b[i] += 1
    c = 0
    for i in range(m):
        if b[i] == 0:
            c = i
            break
    d = 0
    for i in range(m):
        if b[i] > 1:
            d = i
            break
    if c == 0 and d == 0:
        print(0)
        return
    for i in range(m):
        if b[i] == 0:
            c = i
            break
    e = 0
    for i in range(m):
        if b[i] > 1:
            e = i
            break
    if c == 0 and e == 0:
        print(m)
        return
    f = 0
    for i in range(m):
        if b[i] >= 1:
            f += i
    if f == 0:
        print(m)
        return
    g = 0
    for i in range(m):
        if b[i] >= 1:
            g += i
    if g == 0:
        print(m)
        return
    h = 0
    for i in range(m):
        if b[i] >= 2:
            h += i
    if h == 0:
        print(m)
        return
    print(min(f,g,h))
