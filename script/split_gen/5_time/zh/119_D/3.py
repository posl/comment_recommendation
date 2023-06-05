def main():
    a,b,q = map(int,input().split())
    s = [0]*(a+2)
    t = [0]*(b+2)
    x = [0]*q
    for i in range(a):
        s[i+1] = int(input())
    for i in range(b):
        t[i+1] = int(input())
    for i in range(q):
        x[i] = int(input())
    s[0] = t[0] = -10**11
    s[a+1] = t[b+1] = 10**11
    for i in range(q):
        l = 0
        r = a+1
        while r-l > 1:
            m = (l+r)//2
            if s[m] <= x[i]:
                l = m
            else:
                r = m
        l1 = l
        r1 = l+1
        l = 0
        r = b+1
        while r-l > 1:
            m = (l+r)//2
            if t[m] <= x[i]:
                l = m
            else:
                r = m
        l2 = l
        r2 = l+1
        ans = 10**11
        for j in range(2):
            for k in range(2):
                d1 = abs(x[i]-s[l1+j])
                d2 = abs(s[r1-j]-x[i])
                d3 = abs(x[i]-t[l2+k])
                d4 = abs(t[r2-k]-x[i])
                ans = min(ans,max(d1,d2,d3,d4))
        print(ans)
