def solve(n, a):
    ans = []
    for i in range(n):
        ans.append(0)
    for i in range(n):
        ans[a[i]-1] = i+1
    return ans
n = int(input())
a = list(map(int, input().split()))
ans = solve(n, a)
print(*ans)
