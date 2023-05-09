def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = sum(a[i] * (2 * i - n + 1) for i in range(n))
    print(ans)
