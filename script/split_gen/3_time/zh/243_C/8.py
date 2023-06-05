def solve():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    s = input()
    #print(x, y, s)
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            l += 1
        else:
            r += 1
    #print(l, r)
    if l == 0 or r == 0:
        print('No')
        return
    lx = min(x)
    rx = max(x)
    ly = min(y)
    ry = max(y)
    if lx < 0 and rx > 0:
        print('Yes')
        return
    if ly < 0 and ry > 0:
        print('Yes')
        return
    print('No')
solve()
