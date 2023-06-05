def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    c = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m):
        a[i][0] -= 1
        a[i][1] -= 1
        c[i][0] -= 1
        c[i][1] -= 1
    ans = 0
    for i in range(1 << n):
        ok = True
        for j in range(m):
            if ((i >> a[j][0]) & 1) ^ ((i >> a[j][1]) & 1):
                ok = False
        if not ok:
            continue
        now = 0
        for j in range(n):
            if (i >> j) & 1:
                now += 1 << j
        for j in range(m):
            if ((now >> c[j][0]) & 1) ^ ((now >> c[j][1]) & 1):
                ok = False
        if ok:
            ans += 1
    if ans == 1:
        print('Yes')
    else:
        print('No')
