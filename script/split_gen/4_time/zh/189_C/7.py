def solve(n, a):
    max_a = max(a)
    ans = 0
    for x in range(1, max_a + 1):
        for l in range(n):
            for r in range(l, n):
                cnt = 0
                for i in range(l, r + 1):
                    if a[i] >= x:
                        cnt += x
                ans = max(ans, cnt)
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
