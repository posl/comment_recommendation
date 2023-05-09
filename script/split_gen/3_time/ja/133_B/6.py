def solve():
    n,d = map(int,input().split())
    x = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            dis = 0
            for k in range(d):
                dis += (x[i][k]-x[j][k])**2
            if int(dis**0.5)**2 == dis:
                cnt += 1
    print(cnt)
solve()
