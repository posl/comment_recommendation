def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 10**9
    for b in range(-100, 101):
        s = 0
        for i in range(n):
            s += abs(a[i] - (b+i+1))
        ans = min(ans, s)
    print(ans)
