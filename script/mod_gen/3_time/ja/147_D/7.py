def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        zero = 0
        for j in range(n):
            if (a[j] >> i) & 1 == 0:
                zero += 1
        ans += zero * (n - zero) * (1 << i)
        ans %= 10 ** 9 + 7
    print(ans)
solve()
