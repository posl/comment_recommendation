def solve():
    n,a,b,c = map(int,input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10**9
    for i in range(4**n):
        mp = 0
        a1 = a
        b1 = b
        c1 = c
        for j in range(n):
            if i&(1<<j):
                mp += 10
                a1 -= l[j]
            else:
                if j==0:
                    a1 = 0
                mp += 1
        for j in range(n):
            if i&(1<<j):
                if j==0:
                    b1 = 0
                mp += 1
                b1 -= l[j]
            else:
                if j==0:
                    b1 = 0
                mp += 1
        for j in range(n):
            if i&(1<<j):
                if j==0:
                    c1 = 0
                mp += 1
                c1 -= l[j]
            else:
                if j==0:
                    c1 = 0
                mp += 1
        if a1==0 and b1==0 and c1==0:
            ans = min(ans,mp)
    print(ans)
    
solve()
