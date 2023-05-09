def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    k = int(input())
    c = []
    d = []
    for i in range(k):
        ci, di = map(int, input().split())
        c.append(ci)
        d.append(di)
    ans = 0
    for i in range(2 ** k):
        dish = [0 for j in range(n)]
        for j in range(k):
            if (i >> j) & 1:
                dish[c[j] - 1] += 1
            else:
                dish[d[j] - 1] += 1
        count = 0
        for j in range(m):
            if dish[a[j] - 1] > 0 and dish[b[j] - 1] > 0:
                count += 1
        ans = max(ans, count)
    print(ans)
