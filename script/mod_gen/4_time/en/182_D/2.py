def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    x = 0
    for a in A:
        x += a
        ans = max(ans, x)
    return ans
print(solve())
