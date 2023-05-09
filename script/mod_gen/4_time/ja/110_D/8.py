def solve():
    n,m = map(int,input().split())
    ans = 1
    i = 2
    while i*i <= m:
        cnt = 0
        while m % i == 0:
            cnt += 1
            m //= i
        ans *= cnt + 1
        ans %= MOD
        i += 1
    if m != 1:
        ans *= 2
        ans %= MOD
    return ans
MOD = 10**9+7
print(solve())

if __name__ == '__main__':
    solve()