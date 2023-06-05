def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i > 0 and a[i - 1] == a[i]:
            ans += 1
        elif i < n - 1 and a[i] == a[i + 1]:
            ans += 1
    print(ans)
