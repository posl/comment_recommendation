def solve():
    (n, k) = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and stack[-1][0] >= p[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((p[i], i + 1))
        if len(stack) == k:
            stack = []
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    solve()