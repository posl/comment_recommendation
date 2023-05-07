def solve(n,x,ab):
    t = [0]*n
    for i in range(n):
        t[i] = ab[i][0] + ab[i][1]
    for i in range(1,n):
        t[i] = min(t[i],t[i-1]+ab[i][1])
    ans = t[-1]*x
    for i in range(n-2,-1,-1):
        ans = min(ans,t[i]*x+(x-1)*ab[i+1][1])
    return ans

if __name__ == '__main__':
    solve()