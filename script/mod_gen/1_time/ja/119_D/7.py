def solve():
    from bisect import bisect_left,bisect_right
    a,b,q = map(int,input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    s.append(10**11)
    t.append(10**11)
    s.append(-10**11)
    t.append(-10**11)
    s.sort()
    t.sort()
    for i in range(q):
        ans = 10**11
        si = bisect_right(s,x[i])
        sj = bisect_left(s,x[i])
        ti = bisect_right(t,x[i])
        tj = bisect_left(t,x[i])
        for j in [si,sj]:
            for k in [ti,tj]:
                ans = min(ans,abs(x[i]-s[j])+abs(s[j]-t[k]),abs(x[i]-t[k])+abs(t[k]-s[j]))
        print(ans)

if __name__ == '__main__':
    solve()