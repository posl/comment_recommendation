def solve(n, a):
    ans = 0
    for i in range(n):
        if a[i] > ans + 1:
            return ans + 1
        ans += a[i]
    return ans + 1
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(solve(n, a))
