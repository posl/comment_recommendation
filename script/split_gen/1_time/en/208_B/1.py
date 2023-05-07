def solve():
    p = int(input())
    coins = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    ans = 0
    for i in range(10):
        ans += p // coins[i]
        p %= coins[i]
    print(ans)
solve()
