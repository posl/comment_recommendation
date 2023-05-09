def solve(n,k,v):
    ans = 0
    for i in range(min(n,k)+1):
        for j in range(min(n,k)-i+1):
            if i+j > n:
                continue
            t = v[:i] + v[n-j:]
            t.sort()
            ans = max(ans, sum(t[max(0,k-i-j):]))
    return ans

if __name__ == '__main__':
    solve()