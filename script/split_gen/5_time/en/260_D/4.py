def solve(n, k, p):
    ans = [-1]*n
    stack = []
    for i in range(n):
        while stack and stack[-1][0] > p[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((p[i], i+1))
        if len(stack) == k:
            stack = []
    return ans
