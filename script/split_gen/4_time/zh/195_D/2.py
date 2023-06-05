def solve(n,m,q,w,v,x,query):
    ans = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[j-1]>=w[i-1] and query[0]<=j<=query[1]:
                ans = max(ans,v[i-1])
    return ans
