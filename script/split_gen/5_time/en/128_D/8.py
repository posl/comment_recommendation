def solve(n,k,vs):
    ans = 0
    for i in range(min(n+1,k+1)):
        for j in range(min(n+1-i,k+1-i)):
            l = vs[:i]
            r = vs[n-j:]
            l.extend(r)
            l.sort()
            for x in range(min(len(l),k-i-j)):
                if l[x] < 0:
                    l[x] = 0
            ans = max(ans,sum(l))
    return ans
