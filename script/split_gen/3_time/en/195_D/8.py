def solve(n,m,q,w,v,x,l,r):
    ans = []
    for i in range(q):
        ans.append(0)
        for j in range(l[i],r[i]+1):
            x[j-1] = 0
        for j in range(1,2**n):
            sumv = 0
            sumw = 0
            for k in range(n):
                if (j >> k) & 1:
                    sumv += v[k]
                    sumw += w[k]
            if sumw <= x[j-1]:
                ans[i] = max(ans[i],sumv)
        for j in range(l[i],r[i]+1):
            x[j-1] = 1
    return ans
