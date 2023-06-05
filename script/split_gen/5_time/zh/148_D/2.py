def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        if a[i] > n:
            print(-1)
            exit()
        c[a[i] - 1] += 1
    ans = 0
    for i in range(n):
        if c[i] > i + 1:
            print(-1)
            exit()
        ans += i + 1 - c[i]
    print(ans)
solve()
