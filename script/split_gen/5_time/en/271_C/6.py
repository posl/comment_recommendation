def solve():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(N - 1):
        ans += a[i // 2]
    print(ans)
solve()
