def solve():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for p in range(1, 101):
        sum = 0
        for i in range(n):
            sum += (x[i] - p) ** 2
        ans = min(ans, sum)
    print(ans)
solve()
