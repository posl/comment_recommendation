def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    stack = []
    ans = [-1] * n
    for i in range(n):
        while stack and stack[-1][1] < p[i]:
            _, j = stack.pop()
            ans[j-1] = i+1
        stack.append((p[i], i+1))
        if len(stack) == k:
            _, j = stack.pop(0)
            ans[j-1] = i+1
    print(*ans, sep='\n')
