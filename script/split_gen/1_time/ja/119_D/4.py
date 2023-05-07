def main():
    a,b,q = map(int,input().split())
    s = [int(input()) for i in range(a)]
    t = [int(input()) for i in range(b)]
    x = [int(input()) for i in range(q)]
    s.insert(0,0)
    s.append(10000000000000000000)
    t.insert(0,0)
    t.append(10000000000000000000)
    import bisect
    for i in x:
        si = bisect.bisect_left(s,i)
        ti = bisect.bisect_left(t,i)
        ans = 10000000000000000000
        for sj in (s[si-1],s[si]):
            for tj in (t[ti-1],t[ti]):
                ans = min(ans,abs(i-sj)+abs(sj-tj),abs(i-tj)+abs(tj-sj))
        print(ans)
main()
