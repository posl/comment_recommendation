def main():
    A,B,Q = map(int,input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    import bisect
    for i in range(Q):
        s1 = bisect.bisect_left(s,x[i])
        t1 = bisect.bisect_left(t,x[i])
        s2 = bisect.bisect_right(s,x[i])
        t2 = bisect.bisect_right(t,x[i])
        if s1 == 0 and t1 == 0:
            print(max(s[s1],t[t1]) - x[i])
        elif s1 == A and t1 == B:
            print(x[i] - min(s[s1-1],t[t1-1]))
        elif s1 == 0:
            print(min(max(s[s1],t[t1]) - x[i],x[i] - t[t1-1] + max(s[s1],t[t1]) - t[t1-1]))
        elif t1 == 0:
            print(min(max(s[s1],t[t1]) - x[i],x[i] - s[s1-1] + max(s[s1],t[t1]) - s[s1-1]))
        elif s1 == A:
            print(min(x[i] - min(s[s1-1],t[t1-1]) + min(s[s1-1],t[t1-1]) - s[s1-1],x[i] - max(s[s1-1],t[t1-1]) + max(s[s1-1],t[t1-1]) - s[s1-1]))
        elif t1 == B:
            print(min(x[i] - min(s[s1-1],t[t1-1]) + min(s[s1-1],t[t1-1]) - t[t1-1],x[i] - max(s[s1-1],t[t1-1]) + max(s[s1-1],t[t1-1]) - t[t1-1]))
        else:
            print(min(max(s[s1],t[t1]) - x[i],x[i] - s[s1-1] + max(s[s1],t[t1]) - s[s1-1],
