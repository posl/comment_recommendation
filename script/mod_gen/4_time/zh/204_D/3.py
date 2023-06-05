def solve(n, t):
    t.sort(reverse=True)
    ans = [0, 0]
    for i in range(n):
        ans[ans[0] > ans[1]] += t[i]
    return max(ans)
n = int(input())
t = list(map(int, input().split()))
print(solve(n, t))
