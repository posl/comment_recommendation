def solve():
    A, B, K = map(int, input().split())
    ans = 0
    while B > A:
        A *= K
        ans += 1
    print(ans)
