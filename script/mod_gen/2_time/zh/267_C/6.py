def solve(n, m, a):
    #print(n, m, a)
    ans = 0
    for i in range(m):
        ans += (i+1) * a[i]
    #print(ans)
    tmp = ans
    for i in range(m, n):
        tmp = tmp + (i+1) * a[i] - (i-m+1) * a[i-m]
        ans = max(ans, tmp)
        #print(tmp)
    return ans

if __name__ == '__main__':
    solve()