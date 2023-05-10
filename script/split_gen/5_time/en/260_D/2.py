def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1][0] >= p[i]:
            stack.pop()
        if len(stack) > 0:
            ans[i] = stack[-1][1] + 1
        stack.append((p[i], i))
        if len(stack) == k:
            stack = []
    for i in range(n):
        print(ans[i])
