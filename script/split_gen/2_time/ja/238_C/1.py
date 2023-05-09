def solve():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N//(10**i))*(10**(i-1))
        if N%(10**i) >= 10**(i-1):
            ans += 10**(i-1)
        else:
            ans += N%(10**i)+1
    print(ans%MOD)
    return
