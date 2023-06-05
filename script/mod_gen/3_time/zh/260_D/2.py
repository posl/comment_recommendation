def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and p[stack[-1]] > p[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] + 1
        stack.append(i)
        if len(stack) == k:
            stack = []
    for i in range(n):
        print(ans[i])
solve()
