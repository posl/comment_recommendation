def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (10 ** 9 + 1)
    for i in range(n):
        c[a[i]] += 1
    ans = n * (n - 1) // 2
    for i in range(10 ** 9 + 1):
        ans -= c[i] * (c[i] - 1) // 2
    print(ans)
