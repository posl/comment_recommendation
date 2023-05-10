def main():
    n,m,x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = 10**9
    for i in range(2**n):
        tmp = [0]*m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    tmp[k] += a[j][k]
        if min(tmp) >= x:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
