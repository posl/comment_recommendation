def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        c = 0
        for a in A:
            if (a >> i) & 1:
                c += 1
        ans += (1 << i) * c * (N - c)
        ans %= 10 ** 9 + 7
    print(ans)
solve()
