def solve():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    s1 = 0
    ans = S
    for w in W:
        s1 += w
        s2 = S - s1
        ans = min(ans, abs(s1 - s2))
    return ans
print(solve())
