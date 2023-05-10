def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = 10 ** 9
    for i in range(2 ** n):
        tmp = 0
        tmp_a = [0] * m
        for j in range(n):
            if ((i >> j) & 1):
                tmp += c[j]
                for k in range(m):
                    tmp_a[k] += a[j][k]
        if all(x <= tmp_a[k] for k in range(m)):
            ans = min(ans, tmp)
    if ans == 10 ** 9:
        print(-1)
    else:
        print(ans)
