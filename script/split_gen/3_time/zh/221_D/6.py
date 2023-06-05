def solve(n,ab):
    ab.sort(key=lambda x:x[0])
    ans = [0]*n
    for i in range(n):
        a,b = ab[i]
        ans[b-1] += 1
    for i in range(n-2,-1,-1):
        ans[i] += ans[i+1]
    return ans
