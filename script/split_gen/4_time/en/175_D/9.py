def solve(n,k,p,c):
    ans = -1000000000000000000
    for i in range(n):
        s = 0
        t = 0
        j = i
        while True:
            s += c[p[j]-1]
            t += 1
            j = p[j]-1
            if j==i:
                break
        if s > 0:
            u = (k//t-1)*s
            for j in range(k%t):
                u += c[p[(i+j)%n]-1]
            ans = max(ans,u)
        else:
            for j in range(min(k,t)):
                s += c[p[(i+j)%n]-1]
                ans = max(ans,s)
    return ans
