def solve():
    A, B, K = map(int, input().split())
    ans = 0
    while A < B:
        ans += 1
        A *= K
    print(ans)
