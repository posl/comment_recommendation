def solve():
    A, B, T = map(int, input().split())
    ans = 0
    for i in range(1, T + 1):
        if i % A == 0:
            ans += B
    print(ans)
