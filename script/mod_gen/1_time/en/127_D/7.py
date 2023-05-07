def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(m):
        x, y = map(int, input().split())
        b.append(x)
        c.append(y)
    d = []
    for i in range(n):
        d.append([a[i], 1])
    for i in range(m):
        d.append([c[i], b[i]])
    d.sort(reverse=True)
    ans = 0
    cnt = 0
    for i in range(n):
        ans += d[i][0]
    for i in range(n + m):
        if cnt >= n:
            break
        if d[i][1] == 1:
            continue
        for j in range(d[i][1]):
            ans += d[n + j][0] - d[cnt][0]
            cnt += 1
    print(ans)

if __name__ == '__main__':
    main()