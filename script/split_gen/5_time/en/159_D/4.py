def solve():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0
    for i in range(n):
        ans += c[a[i]] - 1
    for i in range(n):
        print(ans - c[a[i]] + 1)
