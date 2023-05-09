def main():
    A,B,Q = map(int,input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    #print(A,B,Q)
    #print(s)
    #print(t)
    #print(x)
    
    import bisect
    INF = 10**11
    s.append(INF)
    s.insert(0,-INF)
    t.append(INF)
    t.insert(0,-INF)
    #print(s)
    #print(t)
    for i in range(Q):
        ans = INF
        now = x[i]
        s_idx = bisect.bisect_left(s,now)
        t_idx = bisect.bisect_left(t,now)
        for j in range(2):
            for k in range(2):
                d1 = abs(now-s[s_idx-j])+abs(s[s_idx-j]-t[t_idx-k])
                d2 = abs(now-t[t_idx-k])+abs(t[t_idx-k]-s[s_idx-j])
                ans = min(ans,d1,d2)
        print(ans)

if __name__ == '__main__':
    main()