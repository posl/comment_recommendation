def solve():
    s = input()
    q = s.count('?')
    mod = 10**9+7
    ans = 0
    for i in range(q+1):
        ans += 3**i * 3**(q-i) * (q-i+1) * (q-i) // 2
        ans %= mod
    print(ans)
solve()
