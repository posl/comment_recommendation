def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = 10**9
    for i in range(2**n):
        tmp = 0
        tmpa = [0]*m
        for j in range(n):
            if (i>>j)&1:
                tmp += c[j]
                for k in range(m):
                    tmpa[k] += a[j][k]
        if min(tmpa)>=x:
            ans = min(ans, tmp)
    if ans==10**9:
        print(-1)
    else:
        print(ans)
