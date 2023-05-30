def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans += a[i] == a[j]
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
