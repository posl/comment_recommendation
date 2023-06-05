def solve(n,q,a,x):
    a.sort()
    x.sort()
    total = sum(a)
    ans = []
    for i in range(q):
        cnt = 0
        for j in range(n):
            if a[j] < x[i]:
                cnt += x[i]-a[j]
        ans.append(total+cnt)
    return ans
