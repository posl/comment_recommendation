def solve(n, k, p):
    ans = [0] * n
    stack = []
    for i in range(n):
        if len(stack) >= k:
            ans[stack.pop()] = i + 1
        while stack and p[stack[-1]] > p[i]:
            stack.pop()
        stack.append(i)
    while stack:
        ans[stack.pop()] = -1
    return ans
n, k = map(int, input().split())
p = list(map(int, input().split()))
print(*solve(n, k, p), sep='\n')

if __name__ == '__main__':
    solve()