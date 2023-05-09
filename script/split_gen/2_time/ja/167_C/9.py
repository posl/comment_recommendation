def main():
    n,m,x = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = 10**9
    for i in range(2**n):
        cost = 0
        u = [0]*m
        for j in range(n):
            if i & (1<<j):
                cost += a[j][0]
                for k in range(m):
                    u[k] += a[j][k+1]
        if min(u) >= x:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
main()
