def solve(n,m):
    if m == 1:
        return 1
    elif n == 1:
        return 1
    else:
        ans = 1
        for i in range(2,int(m**0.5)+1):
            if m % i == 0:
                ans = ans * (m // i + n - 1)
                ans = ans * pow(n-1,mod-2,mod)
                m = m // i
        ans = ans * (m + n - 1)
        ans = ans * pow(n-1,mod-2,mod)
        return ans % mod
mod = 10**9 + 7
n,m = map(int,input().split())
print(solve(n,m))

if __name__ == '__main__':
    solve()