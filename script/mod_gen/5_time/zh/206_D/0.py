def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = {}
    ans = 0
    for i in range(n):
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 1
    for i in range(n):
        if a[i] != a[n - 1 - i]:
            if a[i] in b:
                if b[a[i]] > 1:
                    b[a[i]] -= 1
                else:
                    del b[a[i]]
            if a[n - 1 - i] in b:
                if b[a[n - 1 - i]] > 1:
                    b[a[n - 1 - i]] -= 1
                else:
                    del b[a[n - 1 - i]]
            ans += 1
    print(ans)
solve()
