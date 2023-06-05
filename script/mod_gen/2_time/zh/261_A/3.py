def solve(n, k, p):
    ans = [0] * n
    stack = []
    for i in range(n):
        while stack and stack[-1][0] > p[i]:
            stack.pop()
        if stack and stack[-1][1] >= k:
            ans[i] = stack[-1][2]
        else:
            ans[i] = -1
        stack.append((p[i], i+1, ans[i]))
    return ans
n, k = map(int, input().split())
p = list(map(int, input().split()))
ans = solve(n, k, p)
for i in range(n):
    print(ans[i])

if __name__ == '__main__':
    solve()