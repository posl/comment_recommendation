def solve():
    n = int(input())
    ans = 0
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            ans += 1
    if n > 1:
        ans += 1
    print(ans)
solve()
