def solve(n, k, p):
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and stack[-1][0] >= p[i]:
            if stack[-1][0] == p[i]:
                ans[stack[-1][1]] = i + 1
            stack.pop()
        stack.append((p[i], i))
        if len(stack) == k:
            for j in range(k):
                ans[stack[j][1]] = i + 1
            stack = []
    return ans
n, k = map(int, input().split())
p = list(map(int, input().split()))
ans = solve(n, k, p)
for i in range(n):
    print(ans[i])

if __name__ == '__main__':
    solve()