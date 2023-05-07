def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    r = 10 ** 9
    s1 = 0
    for i in range(n - 1):
        s1 += a[i]
        s -= a[i]
        r = min(r, abs(s1 - s))
    print(r)
solve()
