def solve():
    n = int(input())
    bs = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += min(bs[i], bs[i+1])
    ans += bs[0] + bs[-1]
    print(ans)
